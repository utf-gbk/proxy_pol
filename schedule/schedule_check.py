from .schedule_db import Mongoclient
from proxies_pool.mongo_db import Mongo
import requests
import gevent
from gevent import monkey
from gevent.queue import Queue
import time
mongo_final = Mongo()
mongo = Mongoclient()
# monkey.patch_all()
class IP_Check():

    def validUsefulProxy(self,proxy):
        """
        检验代理是否可用
        :param proxy:
        :return:
        """

        proxies = {"http": "http://{proxy}".format(proxy=proxy)}
        try:
            # 超过20秒的代理就不要了
            r = requests.get('http://httpbin.org/ip', proxies=proxies, timeout=20, verify=False)
            if r.status_code == 200:
                # logger.info('%s is ok' % proxy)
                return True
        except Exception as e:
            # logger.debug(e)
            return False


    def func_judge(self):
        while True:
            try:
                proxy_ip = mongo.pop()
                # print("弹出ip：{}".format(proxy_ip))
                if len(proxy_ip)==0:
                    print("协程等待中")
                    time.sleep(300)
                else:
                    for i in range(0,2):
                        connection = self.validUsefulProxy(proxy_ip)
                        if connection is True:
                            mongo_final.insert(proxy_ip)
                            print("插入freeip到代理池")
                            break
                        # else:
                    #     print("ip无效{}次".format(i+1))
            except:
                continue
                # return None
    # def event(self):
        # p_list = [gevent.spawn(self.func_judge) for i in range(20)]
        # gevent.joinall(p_list)

