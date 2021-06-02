import requests


#暂时只有一句话问答一键点赞
#此次课程为5月23日下午第一节课课前的一句话问答，其他题目需要修改课程id


headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/90.0.4430.72 Safari/537.36 ',
'token': '这里输入自己的token',
# 'Referer': 'http://gxic.itolearn.com/Weixin/QuestionAnswer?icaID=199476530&icid=198780039&scheduleid=113408788&lessionid=198780040',
# 'Accept': 'application/json' 'text/plain' '*/*',
# 'Connection': 'keep-alive',
# 'Host': 'gxic.itolearn.com',
# 'DNT': '1',
# 'Accept-Language': 'zh-CN''zh;q=0.9',
# 'Accept-Encoding': 'gzip' 'deflate'
}

url='http://gxic.itolearn.com/webios/Result'
quesion_url='http://gxic.itolearn.com/api/iCActivities?'
a={
'icid': '198780039',#post请求    http://gxic.itolearn.com/Checkin/GetIccList 返回的值，可能是课程id
'taskIcaID': '199476530',#题目id
# 'scheduleid':'113408788',
# 'lessionid':'198780040'
}


cookies={
'这里输入你的cookies'
}

studen_list=requests.get(url=quesion_url,  cookies=cookies, headers=headers,params=a)
aa=studen_list.json()

cc=[]
for bb in aa['data']['list']:
    cc.append(bb['partake']['AP_ID'])
# print(cc)
# print(len(cc))
for rr in cc:
    ttt=rr
    data = {
        'apIDList' : ttt,  # 个人id
        'icAID' : '199476530',  # 题目id
        'type' : '1',  # 1为点赞，0为取消
    }
    resut = requests.post(url=url, headers=headers, data=data, cookies=cookies)
    print(resut.text)


print(resut.text)