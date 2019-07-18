from django.db import models

class MonitorCampaign(models.Model):
    project_id = models.CharField(blank=True, null=True, max_length=20)
    amount = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    deduction = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    coefficient = models.DecimalField(decimal_places=2, max_digits=3, null=True, blank=True)
    member = models.ForeignKey('MonitorMember', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_id or 'No name'


class MonitorMember(models.Model):
    member_name = models.CharField(blank=True, null=True, max_length=20)
    base_amount = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)

    def __str__(self):
        return self.member_name or 'No name'

    def get_total_amount(self):
        total_amount = self.base_amount
        campaigns = MonitorCampaign.objects.filter(member=self)
        for campaign in campaigns:
            campaign_true_amount = campaign.amount*campaign.coefficient - campaign.deduction*campaign.coefficient
            total_amount += campaign_true_amount
        return total_amount
