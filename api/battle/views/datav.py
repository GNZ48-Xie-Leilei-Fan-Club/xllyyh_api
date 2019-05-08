import json
from django.http import HttpResponse
from django.views import View

from api.models.battle import BattleCampaign


class IndividualView(View):

    def get(self, request):
        all_campaigns = BattleCampaign.objects.all()
        response_array = []
        for campaign in all_campaigns:
            response_array.append(
                {
                    'x': campaign.member_name,
                    'y': float(campaign.amount),
                }
            )
        return HttpResponse(json.dumps(response_array))


class GroupView(View):

    def get(self, request):
        return HttpResponse(json.dumps([{'a':'b'}]))