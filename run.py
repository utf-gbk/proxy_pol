# from proxies_pool.scheduler_proxy import Scheduler
from proxies_pool.get_proxy_api import app
from proxies_pool.requirement import Proxy_get
# def main():
#     s = Scheduler()
#     s.run()
#     print('test')


if __name__ == '__main__':
    # get = Proxy_get()
    # get.get_api()
    app.run('0.0.0.0', 8899,debug=True)
