import json
from collections import OrderedDict
from django.http import HttpResponse
from django.views import View

from api.models.battle import BattleCampaign, BattleGroup


class IndividualBattleBroadcastView(View):

    def get(self, request):
        all_campaigns = BattleCampaign.objects.all().order_by('-amount')
        all_groups = BattleGroup.objects.all()
        if all_campaigns.exists():
            response_text = '当前PK战况(系数前):\n'
            for campaign in all_campaigns:
                response_text += '{}: {} 人数: {}\n'.format(campaign.member_name, campaign.amount, campaign.number_of_participants)
            if all_groups.exists():
                group_result_dict = {}
                for group in all_groups:
                    group_result_dict[group.group_name] = group.total
                response_text += '\n分组战况(系数后):\n'
                print(OrderedDict(sorted(group_result_dict.items(), key=lambda t: t[1])))
                for item in OrderedDict(sorted(group_result_dict.items(), key=lambda t: t[1])):
                    print(item)
                    print(group_result_dict[item])
                    response_text += '{}: {}\n'.format(item, group_result_dict[item])
            
            return HttpResponse(json.dumps({
                'response': response_text,
            }))

        else:
            return HttpResponse(status=404)

