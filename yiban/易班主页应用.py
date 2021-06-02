import requests
import json
import os
import sys
os.chdir(os.path.dirname(__file__))

with open('yibancookie.json', 'r') as f:
    yuanshi = json.load(f)

token = yuanshi['data']['token']
access_token = yuanshi['data']['access_token']

url = 'https://mobile.yiban.cn/api/v3/home'
params = {
    'access_token': access_token
}
header = {
    'Connection': 'keep-alive',
    'Host': 'mobile.yiban.cn',
    'User-Agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/530.17(KHTML,like Gecko) Version/4.0 Mobile Safari/530.17',
    'AppVersion': '4.9.1',
    'Authorization': 'Bearer',
    'loginToken': '',
}
# s = requests.session()
s=requests.get(url=url, params=params, headers=header)

# html_set_cookie = requests.utils.dict_from_cookiejar(s.cookies)
# print(html_set_cookie)

with open('yibanhome.json', 'w')as f:
    f.write(s.text)
