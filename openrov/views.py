from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import LocationForm
from .models import Location

def index(request):
  locations = Location.objects.all()
  
  return render(request, 'openrov/index.html', {
    'MOMENT_DATETIME_FORMAT': settings.MOMENT_DATETIME_FORMAT,
    'locations': locations,
  })

@login_required
def add_location(request):
  if request.method == 'POST':
    location_form = LocationForm(request.POST)

    if location_form.is_valid():
      location_form.save()

      messages.add_message(request, messages.SUCCESS, "The new location record was added successfully.")
      return redirect(reverse('openrov:add_location'))
  else:
    location_form = LocationForm()

  return render(request, 'openrov/add_location.html', {
    'location_form': location_form,
  })
