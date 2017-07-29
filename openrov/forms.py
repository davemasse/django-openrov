from django.forms import ModelForm

from .models import Location

class LocationForm(ModelForm):
  class Meta:
    model = Location
    fields = ['title', 'description', 'lat', 'lng']
