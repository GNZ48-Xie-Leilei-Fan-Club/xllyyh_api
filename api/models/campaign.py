from django_extensions.db.models import TimeStampedModel
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from model_utils import FieldTracker

class Campaign(TimeStampedModel):
    project_id = models.CharField(primary_key=True, max_length=20)
    project_name = models.CharField(blank=True, null=True, max_length=50)
    goal = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    active_since = models.DateTimeField(default=timezone.now, null=False, blank=False)
    is_active_tracker = FieldTracker(fields=['is_active'])


    def save(self, *args, **kwargs):
        if self.is_active_tracker.has_changed('is_active') and self.is_active_tracker.changed()['is_active'] is False:
            self.active_since = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.project_name or 'No name'


class Order(TimeStampedModel):
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    modian_user = models.ForeignKey('ModianUser', blank=True, null=True, on_delete=models.CASCADE)
    campaign = models.ForeignKey('Campaign', blank=True, null=True, on_delete=models.CASCADE)
    transaction = models.OneToOneField('DrawTransaction', null=True, blank=True, on_delete=models.SET_NULL)
    payment_timestamp = models.DateTimeField()


    def __str__(self):
        return '{} : {}'.format(self.modian_user.modian_name, self.amount)