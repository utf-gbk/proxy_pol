from proxies_pool.get_proxy_api import app
if __name__ == '__main__':
    app.run('0.0.0.0', 8999, debug=True)