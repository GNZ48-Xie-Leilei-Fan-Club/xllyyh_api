from django.db import models
from django.utils.translation import gettext_lazy as _


class CardSet(models.Model):
    name = models.CharField()
    is_active = models.BooleanField(default=False)
    cards = models.ManyToManyField('Card', related_name='card_set', null=True, blank=True)


class Card(models.Model):
    name = models.CharField()
    file = models.ImageField(upload_to='cards/')
    rarity = models.ForeignKey('Rarity', blank=False)


class Rarity(models.Model):
    name = models.CharField()
    probability = models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(1)])


class CardUserAssociation(models.Model):
    quantity = models.IntegerField()
    card = models.OneToOneField('Card', related_name='user_profile_association')
    user_profile = models.OneToOneField('UserProfile', related_name='card_association')
