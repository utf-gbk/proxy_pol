from run_app import run_app
from proxies_pool.proxies_source import Proxy_get
from multiprocessing import Process
from schedule.schedule_check import IP_Check
from proxies_pool.getFreeProxy import GetFreeProxy
import gevent
from gevent import monkey

if __name__ == '__main__':
    p = Process(target=run_app)
    p.start()
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
