import datetime
import re
import requests
import time
from optparse import make_option

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone

from openrov.models import Location, Video

PAGE_SIZE = 10
TAG_REGEX = re.compile(r' *#[^ ]+')
VIDEO_REGEX = re.compile(r'(?P<video_url>http://(?:www\.)?youtube.com/watch\?\S*?v=(?P<video_id>[^&\s]+))')

class Command(BaseCommand):
  help = 'Collects remote text via Catch API'
  option_list = BaseCommand.option_list + (
    make_option('-d', '--delete',
      action='store_true',
      dest='delete',
      default=False,
      help='Delete any local Location objects that don\'t exist on the remote side.'),
    )
  
  def handle(self, *args, **options):
    offset = 0
    
    # Get into the loop
    count = PAGE_SIZE
    page_num = 0
    
    while count == PAGE_SIZE:
      params = {
        'full': True,
        'limit': PAGE_SIZE,
        'offset': PAGE_SIZE * page_num,
        'q': '#openrov',
        'sort': 'modified_desc',
      }
      r = requests.get('https://api.catch.com/v2/search.json', params=params, auth=(settings.CATCH_USERNAME, settings.CATCH_PASSWORD))
      data = r.json
      
      count = data['count']
      remote_ids = []
      
      for note in data.get('notes', []):
        remote_id = note['id']
        remote_ids.append(remote_id)
        remote_date_modified = note['server_modified_at']
        remote_date_modified = datetime.datetime.strptime(remote_date_modified, '%Y-%m-%dT%H:%M:%S.%fZ')
        remote_date_modified = remote_date_modified.replace(tzinfo=timezone.utc)
        
        try:
          location = Location.objects.get(remote_id=remote_id)
          # Don't process pre-existing locations that are already up-to-date
          if location.remote_date_modified >= remote_date_modified:
            print '[N] %s' % (remote_id,)
            continue
          else:
            print '[U] %s' % (remote_id,)
        except Location.DoesNotExist:
          location = Location(remote_id=remote_id, remote_date_modified=remote_date_modified)
          print '[C] %s' % (remote_id,)
        
        location.remote_date_created = note['server_created_at']
        location.remote_date_modified = note['server_modified_at']
        location.lat = note['location']['features'][0]['geometry']['coordinates'][1]
        location.lng = note['location']['features'][0]['geometry']['coordinates'][0]
        location.save()
        
        remote_text = note['text'].strip()
        for matches in VIDEO_REGEX.finditer(remote_text):
          Video.objects.get_or_create(location=location, video_id=matches.group('video_id'))
          remote_text = remote_text.replace(' %s' % matches.group('video_url'), '')
        
        location.remote_text = remote_text
        location.description = location.description = TAG_REGEX.sub('', remote_text)
        location.save()
      
      page_num += 1
    
    # Delete Location objects that don't exist remotely
    if options.get('delete') == True:
      to_delete = Location.objects.exclude(remote_id__in=remote_ids)
      'Deleting %s oudated Location objects' % (to_delete.count(),)
      to_delete.delete()