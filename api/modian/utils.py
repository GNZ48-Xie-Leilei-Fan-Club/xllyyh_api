import requests
import json
import urllib
import hashlib
import time
import re
import ast
from decimal import Decimal


class ModianClient():
    def __init__(self, campaign_id):
        self.header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
        self.campaign_id = campaign_id
        self.goal = None
        self.total = None
        self.per_page = 20
        self.order_count_last_scanned = None
        self.campaign_orders_link = 'https://wds.modian.com/api/project/orders'
        self.campaign_detail_link = 'https://zhongchou.modian.com/realtime/get_simple_product?ids={}'
        self.campaign_rankings_link = 'https://wds.modian.com/api/project/rankings'
        self.campaign_amount_link = 'http://orderapi.modian.com/v45/product'
        self.timeout = 15

    def get_signature(self, ret):
        tuple = sorted(ret.items(), key=lambda e: e[0], reverse=False)
        md5_string = urllib.parse.urlencode(tuple).encode(encoding='utf_8', errors='strict')
        md5_string += b'&p=das41aq6'
        signature = hashlib.md5(md5_string).hexdigest()[5: 21]
        return signature

    def orders_link_payload(self, page):
        payload = {
            'page': page,
            'pro_id': int(self.campaign_id),
            'sort_by': 1,
        }
        payload['sign'] = self.get_signature(payload)
        return payload
    
    def detail_link_payload(self):
        payload = {
            'pro_id': int(self.campaign_id),
        }
        payload['sign'] = self.get_signature(payload)
        return payload

    def get_campaign_details(self):
        response = requests.get(self.campaign_detail_link.format(self.campaign_id), timeout=self.timeout)
        json_resp = json.loads(re.search(r"window\[decodeURIComponent\(''\)\]\(\[(.+)\]\)\;", response.text).group(1))
        return json_resp
    
    def get_campaign_orders(self):
        mydict = {}
        data = {
            'pro_id': self.campaign_id,
        }
        response = requests.post(self.campaign_amount_link, data)
        # Return data.
        return_dict = response.json()
        # Return data successfully.
        if return_dict['status'] == '0':
            # Convert string to dictionary.
            return_data = ast.literal_eval(return_dict['data'])

            # Resolve info needed.
            mydict['order_amount'] = return_data['product_info']['backer_money']
            mydict['modian_user_id'] = return_data['product_info']['user_id']
            mydict['modian_user_nickname'] = return_data['product_info']['username']
            mydict['order_timestamp'] = return_data['product_info']['end_time']
            return mydict
        else:
            return {}


def main():
    # import pprint
    client = ModianClient('78370')
    campaign_details = client.get_campaign_details()
    dict = client.get_campaign_orders()
    print(dict)
    print(Decimal(campaign_details['backer_money'].replace(',','')))


if __name__ == '__main__':
    main()
