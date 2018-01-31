from flask import Flask, jsonify, request
from .mongo_db import MongoClient
from .setting import APPS
import json
from flasgger import Swagger

__all__ = ['app']
app = Flask(__name__)
swagger = Swagger(app)

m = MongoClient.collection


@app.route("/")
def index():
    return 'welcome'


def change(http_type):
    if 's' in http_type:
        return 'http'
    else:
        return 'https'


@app.route('/get', methods=['POST'])
def get():
    """this is example
    Get a proxy 从数据库查询多个ip，app_name
    ---
    parameters:
      - name: app_name
        in: path
        type: string
    """
    ip_dict = {
        'ip_list': []
    }
    result_json = request.get_json()
    app_name = result_json['app_name']
    if not app_name:
        return 'loss app_name'
    if app_name not in APPS:
        return 'app_name wrong'
    http_type = APPS[app_name]
    obj_list = m.find({"type": {"$nin": [change(http_type)]}, "apps.{0}".format(app_name): {"$nin": ['0']}}).sort(
        [('time', -1)]).limit(20)
    for i in obj_list:
        ip_dict['ip_list'].append(i['_id'])
    return json.dumps(ip_dict)


@app.route('/update', methods=['POST'])
def update():
    """

    :param : app_name ip is_use
    :return:
    """
    result_json = request.get_json()
    app_name = result_json['app_name']
    ip = result_json['ip']
    is_use = result_json['is_use']
    if not app_name:
        return 'loss app_name'
    if app_name not in APPS:
        return 'app_name wrong'
    http_type = APPS[app_name]
    if is_use is '1':
        m.update({'_id': ip}, {'$set': {'type': http_type}})
    apps = m.find_one({'_id': ip}).get('apps')
    apps[app_name] = is_use
    m.update({'_id': ip}, {'$set': {'apps': apps}})
    return '更新{0}的type成功'.format(ip)


@app.route('/getapps', methods=['GET'])
def get_apps():
    return str(APPS)