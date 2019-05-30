import json
from django.http import HttpResponse
from django.views import View

from api.models.battle import BattleCampaign


class IndividualBattleBroadcastView(View):

    def get(self, request):
        all_campaigns = BattleCampaign.objects.all().order_by('-amount')
        if all_campaigns.exists():
            response_text = '当前PK战况\n'
            for campaign in all_campaigns:
                response_text += '{}: {} 人数: {}\n'.format(campaign.member_name, campaign.amount, campaign.number_of_participants)
            return HttpResponse(json.dumps({
                'response': response_text,
            }))
        else:
            return HttpResponse(status=404)

