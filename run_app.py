from proxies_pool.get_proxy_api import app

def run_app():
    app.run('0.0.0.0', 8999, debug=True)
# if __name__ == '__main__':
