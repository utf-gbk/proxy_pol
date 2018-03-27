**API说明**
--

*api-1: "http://192.168.0.235:8999/get_one_proxy"*
--
用于获取一条代理ip
--
   *post请求参数：app_name*
--
    示例：
    formdata = {"app_name":****}
    proxy_ip = requests.post(api_1,data=formdata).text()
--

*api-2 "http://192.168.0.235:8999/send_proxy_status"*
--
返回当前使用的ip状态
--
post请求参数：
--
app_name
--
status_code(0:当前ip可用;1:当前ip失效)
--
ip  (当前使用ip)
--
示例：
formdata = {"app_name":****,"status_code":0,"ip":*****}
requests.post(api_2,data=formdata)
--

**启动**
接口启动 run_app.py
代理池启动 run_pool.py
