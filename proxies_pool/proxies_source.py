import requests
import json
from .mongo_db import Mongo
import time
mongo = Mongo()
url = "http://dev.kuaidaili.com/api/getproxy/?orderid=982168408884810&num=150&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=1&method=2&an_an=1&an_ha=1&sp2=1&f_sp=1&quality=1&format=json&sep=1"
url_1 = "http://dev.kuaidaili.com/api/getproxy/?orderid=982168408884810&num=200&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=1&method=1&format=json&sep=1"
class Proxy_get():
    def get_api(self):
        while True:
            ip_proxy_json = requests.get(url)
            ip_proxy_dict = json.loads(ip_proxy_json.text)
            ip_more = requests.get(url_1)
            ip_more_dict = json.loads(ip_more.text)
            proxy_list = ip_proxy_dict["data"]["proxy_list"]
            proxy_li = []
            for proxy in proxy_list:
                proxy = proxy.split(",")[0]
                proxy_li.append(proxy)
            mongo.insert(proxy_li)

            proxy_more_li = ip_more_dict["data"]["proxy_list"]
            mongo.insert(proxy_more_li)
            time.sleep(120)