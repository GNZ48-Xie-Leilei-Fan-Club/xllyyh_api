from django.db import models

class KeywordedResponse(models.Model):
    keyword = models.TextField()
    response = models.TextField()

    class JSONAPIMeta:
        resource_name = 'keyworded_responses'
