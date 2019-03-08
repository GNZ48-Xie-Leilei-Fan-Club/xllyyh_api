from django.db import models
from django.utils.translation import gettext_lazy as _

class KeywordedResponse(models.Model):
    keyword = models.TextField(verbose_name=_('关键词'))
    response = models.TextField(verbose_name=_('应答'))

    def __str__(self):
        return self.keyword

    class Meta:
        verbose_name = _('关键词应答')
        verbose_name_plural = _('关键词应答')

    class JSONAPIMeta:
        resource_name = 'keyworded_responses'
