from __future__ import absolute_import, unicode_literals
from celery import task
from django.utils.dateparse import parse_datetime

from .modian.utils import ModianClient
from api.models import Campaign, Order, ModianUser, BattleCampaign

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
                    user, created = ModianUser.objects.get_or_create(modian_id=user_id, modian_name=modian_name)
                    if not Order.objects.filter(amount=amount, modian_user=user, payment_timestamp=payment_timestamp, campaign=campaign).exists() or payment_timestamp < active_since:
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
            campaign.amount = client.get_campaign_details()['data'][0]['already_raised']
            campaign.save()
        except:
            pass