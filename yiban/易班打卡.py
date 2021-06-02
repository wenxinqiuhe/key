import requests
import time
import os,sys
import json
os.chdir(os.path.dirname(__file__))

url = 'https://mobile.yiban.cn/api/v2/passport/login'
params={
    'account':15676901535,
    'passwd':'a%2FvWZpxMYSANLsC9ilg4hKc6vnRb4YxmACkv3S23QzwNu2HCy0X2%2BQKT8tPlL2FE%2FzmrvM3Rt3TzYgX077OmZ0kmFJmBuMQbZaheUzEM1hCPqyELKeLpqbijuCQqzrhWfl4R1F%2FKKLeGsOoF4WLoTof38AmEesmniAAp1uhK6u29v32lXd9fCUtwEijirBksstmpDj8FiuDRdPwOfM%2BJFBqLV%2F90izBFwI%2FyL9JccJzntNlfDniS%2B77RSZB0Lzj%2Bmx0So889UnObaHvSxvGX4ye1Sk2RGjBHVtkRwGZgLVmcz6yvO7VhOni2ju63ZZ7bvlklCxo%2FIFNWb1klBLYDB13EClMRYY4LOZPDDJM9J6gNRdqjushFuVMKTGm8HLgbBpJxJ7j7aZuCyZXsrJ0cOY9gR8hGkNDqruQLIx5K5mSShG0G7PGoXWr1EIxRCVfFclCdvzYBeAIgz3gkBNCkyFG6S0AMrq4SGWHt3bp24MONU8y5lnHuhEz7KTeVC8BuCazCQ9JGtyiW%2Br3wM%2BU5HIOlnnrSkiJdIP%2Fo4VqUCx0oieLIk6PcF890hiQp1d%2FEbM4rdXis6gOFGoh4bgHrreZOCw9vk5URCKKZTK5O7FHy%2BR9oLSvzyShT%2BHcVfXIBdk0RfC2hnGYu8DNeZVJzqasDa%2FRXHWzzL9UYkRCwLdM%3D',
    'ct':2,
    'app':1,
    'v':'4.9.1',
    'apn':'3gnet',
    'identify':597119845045341,
    'sig':'dba414fa2059e403',
    'token':'',
    'device':'Meizu:M6',
    'sversion':24
}
header = {
    'Connection':'keep-alive',
    'Host': 'mobile.yiban.cn',
    'User-Agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/530.17(KHTML,like Gecko) Version/4.0 Mobile Safari/530.17',
    'AppVersion':'4.9.1',
    # 'Authorization':'Bearer',
    # 'loginToken':'',
}

r=requests.get(url=url,params=params,headers=header)
with open('yibancookie.json', 'w')as f:
    f.write(r.text)