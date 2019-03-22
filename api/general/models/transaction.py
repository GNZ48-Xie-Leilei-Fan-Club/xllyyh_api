from django.db import models
from django.utils.translation import gettext_lazy as _

class AbstractTransaction(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField


class DrawTransaction(AbstractTransaction):
    pass