from django.contrib import admin
from .models import Location, Video

class LocationAdmin(admin.ModelAdmin):
    pass

class VideoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Location, LocationAdmin)
admin.site.register(Video, VideoAdmin)
