import requests
import json
from .mongo_db import Mongo
import time
mongo = Mongo()
url = "your ip_proxy api"
url_1 = "your ip_proxy api"
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
