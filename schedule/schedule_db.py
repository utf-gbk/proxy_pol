from pymongo import MongoClient,errors
import datetime
import yaml
import random
setting = yaml.load(open('config.yaml'))

class Mongoclient():
    def __init__(self):
        self.db_name = setting['mongo']['db_name']
        self.collection = setting['mongo']['freeproxy_collection']
        self.conn = MongoClient(host=setting['mongo']['db'], port=setting['mongo']['port'], )


    def mongo_service(self):
        db_name = self.db_name
        collection = self.collection
        db = self.conn[db_name]
        ip_pro = db[collection]
        return ip_pro

    def insert(self,generator):

        ip_pro = self.mongo_service()

        for proxy in generator:
            if proxy:
                try:
                    ip_pro.insert_one({'_id': proxy,
                                       'time': datetime.datetime.now()})
                except errors.DuplicateKeyError as e:

                    print("重复的free_ip!")
                    continue
    def pop(self):
        ip_pro = self.mongo_service()
        try:
            proxy_ip = ip_pro.find_one({})
            proxy_ip = proxy_ip['_id']
            ip_pro.delete_one({"_id":proxy_ip})
            return proxy_ip
        except:
            return None