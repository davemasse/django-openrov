from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

@python_2_unicode_compatible
class Location(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField(null=True, blank=True)
  date_created = models.DateTimeField(auto_now_add=True)
  date_modified = models.DateTimeField(auto_now=True)
  lat = models.DecimalField(max_digits=10, decimal_places=8, null=True, verbose_name='latitude')
  lng = models.DecimalField(max_digits=11, decimal_places=8, null=True, verbose_name='longitude')
  
  class Meta:
    ordering = ('-date_created',)
    verbose_name = _('location')
    verbose_name_plural = _('locations')

  def __str__(self):
    return '%s (%s,%s)' % (self.title, self.lat, self.lng,)

@python_2_unicode_compatible
class Video(models.Model):
  location = models.ForeignKey(Location)
  video_id = models.CharField(max_length=100, null=True, blank=True)
  
  class Meta:
    ordering = ('video_id',)
    verbose_name = _('video')
    verbose_name_plural = _('videos')
  
  def __str__(self):
    return self.video_id
