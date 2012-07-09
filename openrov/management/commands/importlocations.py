import base64
import datetime
import re
import simplejson
import time
import urllib2

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone

from openrov.models import Location, Video

class Command(BaseCommand):
  help = 'Collects remote text via Catch API'
  
  def handle(self, *args, **options):
    request = urllib2.Request('https://api.catch.com/v2/search.json?q=#openrov&sort=modified_asc&limit=1000')
    base64string = base64.encodestring('%s:%s' % (settings.CATCH_USERNAME, settings.CATCH_PASSWORD)).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)   
    result = urllib2.urlopen(request)
    data = simplejson.loads(result.read())
    
    notes = data.get('notes', [])
    
    for note in notes:
      remote_id = note['id']
      remote_date_modified = note['server_modified_at']
      remote_date_modified = datetime.datetime.strptime(remote_date_modified, '%Y-%m-%dT%H:%M:%S.%fZ')
      remote_date_modified = remote_date_modified.replace(tzinfo=timezone.utc)
      
      try:
        location = Location.objects.get(remote_id=remote_id)
        
        # Don't process pre-existing locations that are already up-to-date
        if location.remote_date_modified >= remote_date_modified:
          continue
      except Location.DoesNotExist:
        location = Location(remote_id=remote_id, remote_date_modified=remote_date_modified)
      
      request = urllib2.Request('https://api.catch.com/v2/notes/%s.json' % remote_id)
      request.add_header("Authorization", "Basic %s" % base64string)   
      result = urllib2.urlopen(request)
      data = simplejson.loads(result.read())
      
      remote_note = data['notes'][0]
      remote_date_created = remote_note['server_created_at']
      remote_text = remote_note['text'].strip()
      lat = remote_note['location']['features'][0]['geometry']['coordinates'][1]
      lng = remote_note['location']['features'][0]['geometry']['coordinates'][0]
      
      location.remote_date_created = remote_date_created
      location.lat = lat
      location.lng = lng
      location.save()
      
      for matches in re.finditer(r'(?P<video_url>http://(?:www\.)?youtube.com/watch\?\S*?v=(?P<video_id>[^&\s]+))', remote_text):
        Video.objects.get_or_create(location=location, video_id=matches.group('video_id'))
        remote_text = remote_text.replace(' %s' % matches.group('video_url'), '')
      location.remote_text = remote_text
      location.description = location.description = re.sub(r' *#[^ ]+', '', remote_text)
      location.save()