from django.conf.urls import patterns, include, url

urlpatterns = patterns('openrov.views',
  (r'^$', 'index', {}, 'index'),
)