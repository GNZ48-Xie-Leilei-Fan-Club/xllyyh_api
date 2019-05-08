from django.db import models

class BattleCampaign(models.Model):
    project_id = models.CharField(primary_key=True, max_length=20)
    member_name = models.CharField(blank=True, null=True, max_length=50)
    amount = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    coefficient = models.DecimalField(decimal_places=2, max_digits=3, null=True, blank=True)

    def __str__(self):
        return self.member_name or 'No name'
