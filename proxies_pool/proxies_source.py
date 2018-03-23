import requests
import json
from .mongo_db import Mongo
import time
mongo = Mongo()
url = "http://dev.kuaidaili.com/api/getproxy/?orderid=982168408884810&num=200&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=1&method=2&an_an=1&an_ha=1&sp2=1&f_sp=1&quality=1&sort=1&format=json&sep=1"
class Proxy_get():
    def get_api(self):
        while True:
            ip_proxy_json = requests.get(url)
            ip_proxy_dict = json.loads(ip_proxy_json.text)
            proxy_list = ip_proxy_dict["data"]["proxy_list"]
            print(proxy_list)
            mongo.insert(proxy_list)
            time.sleep(600)