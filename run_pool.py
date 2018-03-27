from proxies_pool.get_proxy_api import app
from proxies_pool.proxies_source import Proxy_get
from multiprocessing import Process
from schedule.schedule_check import IP_Check
from proxies_pool.getFreeProxy import GetFreeProxy
import gevent
from gevent import monkey


if __name__ == '__main__':
    monkey.patch_all()
    get = Proxy_get()
    p1 = Process(target=get.get_api)
    p1.start()
    check = IP_Check()
    getfreeip = GetFreeProxy()
    p2 = Process(target=getfreeip.start)
    p2.start()

    p_list = [gevent.spawn(check.func_judge) for i in range(500)]

    gevent.joinall(p_list)
    # app.run('0.0.0.0',8999,debug=True)

