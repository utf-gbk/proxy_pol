import requests


class TK:
    # todo 把两个的数量修改成100个
    result_http = requests.get(
        'http://api.tkdaili.com/api/getiplist.aspx?vkey=2D1707097D5E4DA1A65E362BE4F988FB&num=200&country=CN&speed=5000&high=1&https=1&style=2')

    def get_http_proxy_list(self):
        """

        :return:['185.82.201.112:1080', '220.167.108.155:8088', '223.96.95.229:3128', ]
        """
        result = self.result_http.content.decode()
        print(result.split('\n'))
        return result.split('\n')


if __name__ == '__main__':
    t = TK()
    t.get_http_proxy_list()
