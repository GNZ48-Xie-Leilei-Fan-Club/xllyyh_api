from django.db import models
from django.utils.translation import gettext_lazy as _

class Campaign(models.Model):
    project_id = models.CharField(primary_key=True, max_length=20)
    goal = models.DecimalField(decimal_places=2, max_digits=10)
    amount = models.DecimalField(decimal_places=2, max_digits=10)


class Order(models.Model):
    order_id = models.CharField(primary_key=True, max_length=20)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    user_profile = models.ForeignKey('UserProfile', blank=False, on_delete=models.CASCADE)
    campaign = models.ForeignKey('Campaign', blank=False, on_delete=models.CASCADE)
    transaction = models.OneToOneField('DrawTransaction', null=True, blank=True, on_delete=models.SET_NULL)
    timestamp = models.DateTimeField()
