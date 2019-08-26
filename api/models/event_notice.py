from django_extensions.db.models import TimeStampedModel
from django.db import models


class NewMemberNotice(TimeStampedModel):
    title = models.CharField(max_length=20)
    response = models.TextField()

    def __str__(self):
        return self.title

    class JSONAPIMeta:
        resource_name = 'new_member_notice'
