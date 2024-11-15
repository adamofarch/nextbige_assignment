from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save
from django.conf import settings

class User(AbstractUser):
    phone_number = models.CharField(
        max_length=14,
        validators=[
            RegexValidator(
                regex=r'^(\+91 )?[6-9]\d{9}$',
                message='Enter a Valid phone number'
            )
        ]
    )
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    last_login_ip = models.GenericIPAddressField(null=True, blank=True)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
