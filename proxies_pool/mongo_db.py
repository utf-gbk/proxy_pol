from pymongo import MongoClient, errors
import pymongo
import datetime
import yaml
import random
setting = yaml.load(open('config.yaml'))


class Mongo():
    def __init__(self):
        self.db_name = setting['mongo']['db_name']
        self.collection = setting['mongo']['collection_name']
        self.conn = MongoClient(host=setting['mongo']['db'], port=setting['mongo']['port'],)

    def insert(self,proxies):
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

        if type(proxies) == list:
            for proxy in proxies:
                try:
                    ip_pro.create_index([("time",pymongo.ASCENDING)], expireAfterSeconds=3*24*60*60)
                    ip_pro.insert_one({'_id': proxy,
                                        'time': datetime.datetime.utcnow(),
                                       'source': 'KuaiDaiLi'})
                except errors.DuplicateKeyError as e:
                    print(e)
                    print('重复的proxy_ip:{}'.format(proxy))
                    continue
        else:
            try:
                ip_pro.create_index([("time", pymongo.ASCENDING)], expireAfterSeconds=3*24*60*60)
                ip_pro.insert_one({'_id': proxies,
                                  'time': datetime.datetime.utcnow(),
                                   'source': 'Other'})
            except errors.DuplicateKeyError as e:
                print(e)
                print('重复的active_free_ip')
                print(proxies)



    def find(self,app_name):
        db_name = self.db_name
        collection = self.collection
        db = self.conn[db_name]
        ip_pro = db[collection]
        ip_list = ip_pro.find({app_name:{"$nin":[1]}}).sort('time',-1).limit(20)
            # .sort([('time', -1)]).limit(20)

        return ip_list[random.randint(0,19)]['_id']

    def update(self,app_name,ip,status_code):
        db_name = self.db_name
        collection = self.collection
        db = self.conn[db_name]
        ip_pro = db[collection]

        ip_pro.update({"_id":ip},{"$set":{app_name:status_code}},True)


        print("更新成功")
