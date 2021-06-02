import requests
import json
import os,sys
os.chdir(os.path.dirname(__file__))

with open('yibanhome.json', 'r')as f:
    yuanshi=json.load(f)
# print(yuanshi['data']['hotApps'][10]['url'])
header = {
    'Connection':'keep-alive',
    'Host': 'mobile.yiban.cn',
    'User-Agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/530.17(KHTML,like Gecko) Version/4.0 Mobile Safari/530.17',
    'AppVersion':'4.9.1',
    'Authorization':'Bearer',
    'loginToken':'',
}
# # s=requests.session()
s=requests.get(url=yuanshi['data']['hotApps'][10]['url'],headers=header)
html_set_cookie = requests.utils.dict_from_cookiejar(s.cookies)
print(html_set_cookie)
# print(yuanshi['data']['hotApps'][9])