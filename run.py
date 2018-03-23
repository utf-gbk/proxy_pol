from proxies_pool.get_proxy_api import app
from proxies_pool.proxies_source import Proxy_get
from multiprocessing import Process


if __name__ == '__main__':
    get = Proxy_get()
    p = Process(target=get.get_api)
    p.start()
    app.run('0.0.0.0', 8999,debug=True)
