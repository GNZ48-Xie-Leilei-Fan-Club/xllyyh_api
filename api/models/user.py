from django.contrib.auth.models import AbstractUser
from django.db import models
from django_extensions.db.models import TimeStampedModel

class FanClubUser(AbstractUser, TimeStampedModel):
    qq_number = models.CharField(max_length=50)
    modian_user = models.ForeignKey('ModianUser', blank=True, null=True, on_delete=models.SET_NULL)


class ModianUser(TimeStampedModel):
    modian_id = models.CharField(max_length=50)
    modian_name = models.CharField(max_length=50)
    cards = models.ManyToManyField('Card', through='CardUserAssociation')

