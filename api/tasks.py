from __future__ import absolute_import, unicode_literals
from celery import task
from django.utils.dateparse import parse_datetime
from decimal import Decimal

from .modian.utils import ModianClient
from api.models import Campaign, Order, ModianUser, BattleCampaign, MonitorCampaign

@task()
def fetch_modian_campaign_orders():
    all_active_campaigns = Campaign.objects.filter(is_active=True)
    for campaign in all_active_campaigns:
        project_id = campaign.project_id
        active_since = campaign.active_since
        client = ModianClient(project_id)
        no_new_orders = False
        page = 1
        while not no_new_orders:
            try:
                orders = client.get_campaign_orders(page)['data']
                for order in orders:
                    amount = order['backer_money']
                    user_id = order['user_id']
                    payment_timestamp = parse_datetime(order['pay_time'])
                    modian_name = order['nickname']
                    user, created = ModianUser.objects.get_or_create(modian_id=user_id)
                    if not created:
                        if user.modian_name != modian_name:
                            user.modian_name = modian_name
                            user.save()
                    if not Order.objects.filter(amount=amount, modian_user=user, payment_timestamp=payment_timestamp, campaign=campaign).exists():
                        order = Order.objects.create(amount=amount, modian_user=user, payment_timestamp=payment_timestamp, campaign=campaign)
                    else:
                        no_new_orders = True
                page += 1
            except:
                break


@task()
def fetch_battle_campaign_details():
    all_battle_campaigns = BattleCampaign.objects.all()
    for campaign in all_battle_campaigns:
        project_id = campaign.project_id
        client = ModianClient(project_id)
        try:
            campaign_details = client.get_campaign_details()
            campaign.amount = Decimal(campaign_details['backer_money'].replace(',',''))
            campaign.number_of_participants = campaign_details['backer_count']
            campaign.save()
        except:
            pass


@task()
def fetch_monitor_campaign_details():
    all_monitor_campaigns = MonitorCampaign.objects.all()
    for campaign in all_monitor_campaigns:
        project_id = campaign.project_id
        client = ModianClient(project_id)
        try:
            campaign_details = client.get_campaign_details()['data'][0]
            campaign.amount = campaign_details['already_raised']
            campaign.save()
        except:
            pass
