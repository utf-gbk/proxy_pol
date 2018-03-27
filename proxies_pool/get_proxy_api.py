import json
from flask import Flask, jsonify, request
from .mongo_db import Mongo


__all__ = ['app']
app = Flask(__name__)
# url = "http://dev.kuaidaili.com/api/getproxy/?orderid=982168408884810&num=50&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=1&method=2&an_an=1&an_ha=1&sp2=1&quality=1&sort=1&format=json&sep=1"
mongo = Mongo()


@app.route("/get_one_proxy",methods=['POST'])
def get_proxy():
    # result_json = request.get_json()
    if not request.form['app_name']:
        return '传参错误！'
    # status_bol = result_json['status_code']
    print(request.form['app_name'])
    try:
        positive_ip = mongo.find(request.form['app_name'])
        return positive_ip
    except:
        return "no ip can be used!"


@app.route("/send_proxy_status",methods=['POST'])
def send_proxy():
    try:
        app_name = request.form['app_name']
        status_code = request.form['status_code']
        ip = request.form['ip']
        status_code = int(status_code)
        try:
            mongo.update(app_name,ip,status_code)
        except:
            return "ip地址错误！"
        return "sucess!"
    except:
        print("参数错误！")

