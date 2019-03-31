from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator


class CardSet(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)


class Card(models.Model):
    name = models.CharField(max_length=50)
    file = models.ImageField(upload_to='cards/')
    rarity = models.ForeignKey('Rarity', null=True, blank=True, on_delete=models.SET_NULL)
    card_set = models.ForeignKey('CardSet', related_name='cards', null=True, blank=True, on_delete=models.SET_NULL)


class Rarity(models.Model):
    name = models.CharField(max_length=50)
    probability = models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(1)])


class CardUserAssociation(models.Model):
    quantity = models.IntegerField()
    card = models.ForeignKey('Card', on_delete=models.CASCADE)
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
