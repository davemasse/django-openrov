django.db.models.signals import post_save

from openrov.models import Location

def process_remote_text(sender, instance, signal):
  print instance

post_save.connect(process_remote_text, sender=Location)