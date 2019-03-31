from django.db import models
from django.utils.translation import gettext_lazy as _

class Transaction(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField('Card', through='CardTransactionAssociation')


class DrawTransaction(Transaction):
    pass

class CardTransactionAssociation(models.Model):
    quantity = models.IntegerField()
    card = models.ForeignKey('Card', on_delete=models.CASCADE)
    transaction = models.ForeignKey('Transaction', on_delete=models.CASCADE)
