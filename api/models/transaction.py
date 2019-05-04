from django_extensions.db.models import TimeStampedModel
from django.db import models
from django.utils.translation import gettext_lazy as _

class Transaction(TimeStampedModel):
    products = models.ManyToManyField('Card', through='CardTransactionAssociation')


class DrawTransaction(Transaction):
    pass

class CardTransactionAssociation(TimeStampedModel):
    quantity = models.IntegerField()
    card = models.ForeignKey('Card', on_delete=models.CASCADE)
    transaction = models.ForeignKey('Transaction', on_delete=models.CASCADE)
