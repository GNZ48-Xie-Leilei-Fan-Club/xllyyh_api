import json
import requests as re
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
                for item in OrderedDict(sorted(group_result_dict.items(), key=lambda t: t[1], reverse=True)):
                    response_text += '{}: {}\n'.format(item, group_result_dict[item])
            
            return HttpResponse(json.dumps({
                'response': response_text,
            }))

        else:
            return HttpResponse(status=404)


class TotalRankingsView(View):

    def get(self, request):
        try:
            raw_response = re.get('https://www.jzb48.com/api/main_table.php').json()
            parsed_rankings = []
            for ranking in range(1,17):
                individual_json = json.loads(raw_response['rank{}'.format(ranking)])
                parsed_rankings.append(
                    (
                        ranking,
                        individual_json['member'] if individual_json['member'] == '谢蕾蕾' else None,
                        individual_json['real_amount'],
                    )
                )
            response_rankings = []
            for item in parsed_rankings:
                if (item[1] == '谢蕾蕾'):
                    index = parsed_rankings.index(item)
                    response_rankings.append(parsed_rankings[index-2])
                    response_rankings.append(parsed_rankings[index-1])
                    response_rankings.append(item)
                    response_rankings.append(parsed_rankings[index+1])
                    response_rankings.append(parsed_rankings[index+2])
            response_text = '实时集资排名:\n'
            for item in response_rankings:
                if item[1]:
                    response_text += '{}.{}: {}\n'.format(item[0], item[1], item[2])
                else:
                    response_text += '{}: {}\n'.format(item[0], item[2])
            return HttpResponse(json.dumps({
                'response': response_text,
            }))
        except:
            return HttpResponse(status=404)
