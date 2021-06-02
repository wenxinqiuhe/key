import json
import requests
import time
from account import seq_se

with open('cookie.json','r')as f:
    cookie=json.load(f)
header=seq_se().header
print(cookie)
dates = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())
xurl = 'http://gxic.itolearn.com/Weixin/Schedule'
params = {
    '_date': dates,
    '_ver': '3.2.0.2'
}
rs = requests.get(xurl, params=params, headers=header, cookies=cookie)
# html_set_cookie = requests.utils.dict_from_cookiejar(rs.cookies)
print(rs.text)