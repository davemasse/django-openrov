from django.db import models
from django.utils.translation import ugettext_lazy as _

class Location(models.Model):
  remote_id = models.CharField(max_length=100, unique=True)
  remote_text = models.TextField(null=True, blank=True)
  remote_date_created = models.DateTimeField(null=True, blank=True)
  remote_date_modified = models.DateTimeField()
  description = models.TextField(null=True, blank=True)
  lat = models.DecimalField(max_digits=10, decimal_places=8, null=True, verbose_name='latitude')
  lng = models.DecimalField(max_digits=11, decimal_places=8, null=True, verbose_name='longitude')
  
  class Meta:
    ordering = ('-remote_date_created',)
    verbose_name = _('location')
    verbose_name_plural = _('locations')
  
  def __unicode__(self):
    return self.remote_id

class Video(models.Model):
  location = models.ForeignKey(Location)
  video_id = models.CharField(max_length=100, null=True, blank=True)
  
  class Meta:
    ordering = ('video_id',)
    verbose_name = _('video')
    verbose_name = _('videos')
  
  def __unicode__(self):
    return self.video_id