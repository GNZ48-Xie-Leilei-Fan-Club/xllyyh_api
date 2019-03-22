from django.db import models
from django.utils.translation import gettext_lazy as _

class Campaign(models.Model):
    project_id = models.CharField(primary_key=True)
    goal = models.DecimalField()
    amount = models.DecimalField()


class Order(models.Model):
    order_id = models.CharField(primary_key=True)
    amount = models.DecimalField()
    user_profile = models.ForeignKey('UserProfile', blank=False)
    campaign = models.ForeignKey('Campaign', blank=False)
    transaction = models.OneToOneField('DrawTransaction', related_name='order', blank=False)
    timestamp = models.DateTimeField()
