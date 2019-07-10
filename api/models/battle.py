from django.db import models

class BattleCampaign(models.Model):
    project_id = models.CharField(blank=True, null=True, max_length=20)
    member_name = models.CharField(blank=True, null=True, max_length=50)
    amount = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    coefficient = models.DecimalField(decimal_places=2, max_digits=3, null=True, blank=True)
    number_of_participants = models.IntegerField(null=True, blank=True)
    battle_group = models.ForeignKey('BattleGroup', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.member_name or 'No name'

class BattleGroup(models.Model):
    group_name = models.CharField(blank=True, null=True, max_length=20)

    @property
    def total(self):
        total = 0
        for campaign in BattleCampaign.objects.filter(battle_group=self):
            total += campaign.amount * campaign.coefficient
        return total
    
    def __str__(self):
        return self.group_name or 'No name'

class BattleNotification(models.Model):
    message = models.CharField(blank=True, null=True, max_length=500)
