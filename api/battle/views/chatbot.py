import json
from django.http import HttpResponse
from django.views import View

from api.models.battle import BattleCampaign


class IndividualBattleBroadcastView(View):

    def get(self, request):
        all_campaigns = BattleCampaign.objects.all().order_by('-amount')
        response_text = '当前PK战况\n'
        for campain in all_campaigns:
            response_text += '{}: {}\n'.format(campain.member_name, campain.amount)
        return HttpResponse(json.dumps({
            'response': response_text,
        }))

