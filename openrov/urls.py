from django.conf.urls import include, url

from . import views

app_name = 'openrov'
urlpatterns = [
  url(r'^$', views.index, {}, 'index'),
  url(r'^add-location$', views.add_location, {}, 'add_location'),
]
