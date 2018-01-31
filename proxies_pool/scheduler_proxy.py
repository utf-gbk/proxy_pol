from .mongo_db import MongoClient
from .proxy_source import TK
from .app import app
from multiprocessing import Process
import time


class Scheduler:
    db_client = MongoClient()

    def scheduler_http_insert(self):
        """
        定时插入http代理
        :return:
        """
        while True:
            tk = TK()
            proxy_list = tk.get_http_proxy_list()
            self.db_client.insert(proxy_list, )
            print(proxy_list)
            print('insert success')
            time.sleep(1800)

    @staticmethod
    def scheduler_api():
        """
        开启api服务
        :return:
        """
        app.run(host='0.0.0.0', port=6002)

    def run(self):
        # Process(target=self.scheduler_delete).start()
        # Process(target=self.scheduler_http_insert).start()
        Process(target=self.scheduler_api).start()
