from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, blank=False, on_delete=models.CASCADE)
    modian_id = models.CharField(max_length=50)
    qq_number = models.CharField(max_length=50)
    cards = models.ManyToManyField('Card', through='CardUserAssociation')
