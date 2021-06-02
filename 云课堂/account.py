import requests
import os
import json
os.chdir(os.path.dirname(__file__))


class seq_se:
    def __init__(self):
        self.header = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 7.0; M6 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045614 Mobile Safari/537.36 MMWEBID/5002 MicroMessenger/7.0.1380(0x27000034) Process/tools NetType/4G Language/zh_CN",
            "Host": "gxic.itolearn.com",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "X-Requested-With": "com.tencent.mm",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
        }

    def cookie(self):
        s = requests.session()
        cookie = {'token': ''}
        datas = {
            'code': '191040330125',
            'pwd': 'qfz200112'
        }
        xxs = s.post('http://gxic.itolearn.com/Account/LoginProcess',data=datas, headers=self.header)
        text = json.loads(xxs.text)
        cookie['token'] = text['token']
        html_set_cookie = requests.utils.dict_from_cookiejar(xxs.cookies)
        cookie.update(html_set_cookie)
        return cookie


def wr():
    cookie = seq_se().cookie()
    with open('cookie.json', 'w')as f:
        f.write(str(json.dumps(cookie)))


if __name__ == '__main__':
    wr()
# cookie = session()
# dates = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())
# xurl = 'http://gxic.itolearn.com/Weixin/Schedule'
# params = {
#     '_date': dates,
#     '_ver': '3.2.0.2'
# }
# rs = requests.get(xurl, params=params, headers=header, cookies=cookie)
# # html_set_cookie = requests.utils.dict_from_cookiejar(rs.cookies)
# print(rs.text)
