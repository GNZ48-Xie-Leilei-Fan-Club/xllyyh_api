from django_extensions.db.models import TimeStampedModel
from django.db import models
from django.utils.translation import gettext_lazy as _

class KeywordedResponse(TimeStampedModel):
    keyword = models.TextField(verbose_name=_('关键词'))
    response = models.TextField(verbose_name=_('应答'))

    def __str__(self):
        return self.keyword

    class Meta:
        verbose_name = _('关键词应答')
        verbose_name_plural = _('关键词应答')

    class JSONAPIMeta:
        resource_name = 'keyworded_responses'


class IgnoreNumber(TimeStampedModel):
    number = models.TextField(verbose_name='QQ号', max_length=30)
    note = models.TextField(verbose_name='备注')

    def __str__(self):
        return self.number
    
    class Meta:
        verbose_name = _('忽略QQ号')
        verbose_name_plural = _('忽略QQ号')

    class JSONAPIMeta:
        resource_name = 'ignore_numbers'
