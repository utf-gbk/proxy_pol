from pymongo import MongoClient, errors
import datetime
import yaml
import random
setting = yaml.load(open('config.yaml'))


class Mongo():
    def __init__(self):
        self.db_name = setting['mongo']['db_name']
        self.collection = setting['mongo']['collection_name']
        self.conn = MongoClient(host=setting['mongo']['db'], port=setting['mongo']['port'],)

    def insert(self,proxies_list):
        """
        定时从数据源添加一组代理
        apps: apps:{name:amap, score:0}
        http_type: http, https
        :param proxies_list: [0.0.0.0, 1.1.1.1]
        :return:
        """
        db_name = self.db_name
        collection = self.collection
        db = self.conn[db_name]
        ip_pro = db[collection]

        for proxy in proxies_list:
            if proxy:
                try:
                    ip_pro.insert_one({'_id': proxy,
                                        'time': datetime.datetime.now()})
                except errors.DuplicateKeyError as e:
                    print(e)
                    print('重复的数据')
                    print(proxy)
                    continue

    def find(self,app_name):
        db_name = self.db_name
        collection = self.collection
        db = self.conn[db_name]
        ip_pro = db[collection]
        ip_list = ip_pro.find({app_name:{"$nin":["False"]}}).sort('time',-1).limit(20)
            # .sort([('time', -1)]).limit(20)

        return ip_list[random.randint(0,19)]['_id']

    def update(self,app_name,ip,status_code):
        db_name = self.db_name
        collection = self.collection
        db = self.conn[db_name]
        ip_pro = db[collection]

        ip_pro.update({"_id":ip},{app_name:status_code},True)
