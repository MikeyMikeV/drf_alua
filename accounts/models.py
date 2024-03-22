from django.db import models

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Create your models here.
from django.dispatch import receiver
from django.db.models import signals

@receiver(signal=signals.post_save, sender = User)
def create_auth_token(sender, instance, created=False, **kwargs):
    if created:
        Token.objects.create(user = instance)