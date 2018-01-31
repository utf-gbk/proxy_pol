from pymongo import MongoClient, errors
import datetime

client = MongoClient('192.168.0.235', 27017)
db = client['proxies']


class MongoClient:
    collection = db['proxies']

    def insert(self, proxies_list, ):
        """
        定时从数据源添加一组代理
        apps: apps:{name:amap, score:0}
        http_type: http, https
        :param proxies_list: [0.0.0.0, 1.1.1.1]
        :return:
        """
        for proxy in proxies_list:
            if proxy:
                try:
                    self.collection.insert_one({'_id': proxy,
                                                'apps': {},
                                                'type': None,
                                                'time': datetime.datetime.now()})
                except errors.DuplicateKeyError as e:
                    print('重复的数据')
                    print(proxy)
                    continue
