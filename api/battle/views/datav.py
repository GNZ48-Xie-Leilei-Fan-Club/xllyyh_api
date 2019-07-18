import json
from django.http import HttpResponse
from django.views import View

from api.models.battle import BattleCampaign, BattleNotification
from api.models.monitor import MonitorMember


class IndividualView(View):

    def get(self, request):
        all_campaigns = BattleCampaign.objects.all().order_by('-amount')[:7]
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


class NotificationView(View):

    def get(self, request):
        message = BattleNotification.objects.all().first().message
        return HttpResponse(json.dumps([{'value': message}]))


class MonitorView(View):

    def get(self, request):
        all_members = MonitorMember.objects.all().order_by('-base_amount')[:7]
        response_array = []
        for member in all_members:
            response_array.append(
                {
                    'x': member.member_name,
                    'y': float(member.get_total_amount()),
                }
            )
        return HttpResponse(json.dumps(response_array))