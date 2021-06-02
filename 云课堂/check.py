from collections import namedtuple
import requests
import json
#import os
# os.chdir(os.path.dirname(__file__))
from account import seq_se

with open('cookie.json', 'r')as f:
    cookie = json.load(f)
header = seq_se().header
url = 'http://gxic.itolearn.com/Checkin/CheckIn'
data = {
    'CheckInType': '1',
    'Code': '158907'
}
s = requests.session()
s.headers = header
requests.utils.add_dict_to_cookiejar(s.cookies, cookie)
r = s.post(url=url, data=data)
addcookie = json.loads(r.text)
# 添加笔记
addnote={"Content":".","IC_ID":addcookie['data']['IC_ID'],"ID":0,"userId":"52272721","fileID":[]}
for x in range(5):
	rr=s.post(url='http://gxic.itolearn.com/HomeNote/AddAnsterNote',data=addnote)
	print(rr.text)
# 遍历课前课中课后
for a in range(1, 4):
    postdata = {
        "applayType": a,
        "ic_id": addcookie['data']['IC_ID'],
        "batchid": None,
        "schduleid": addcookie['data']['Schedule_Id'][0],
        "lessionid": addcookie['data']['Lessons_ID']
    }
    headere = {
        "icid": str(addcookie['data']['IC_ID']),
        "scheduleid": str(addcookie['data']['Schedule_Id'][0]),
        "lessionid": str(addcookie['data']['Lessons_ID'])
    }
    requests.utils.add_dict_to_cookiejar(s.cookies, headere)
    cr = s.post('http://gxic.itolearn.com/Weixin/partialItemClassJson?v=60', data=postdata)
    list = json.loads(cr.text)
    if len(list['items']) != 0:
        for b in range(len(list['items'])):
            if list['items'][b]['typeId'] == '3':
                quesion_url = 'http://gxic.itolearn.com/api/iCActivities'
                da = {
                    'icid': str(addcookie['data']['IC_ID']),
                    'taskIcaID': str(list['items'][b]['ID'])  # 题目id
                }
                co = {'token': requests.utils.dict_from_cookiejar(s.cookies)['token']}
                s.headers.update(co)
                studen_list = s.get(url=quesion_url, params=da)
                yun = json.loads(studen_list.text)
                name = {'覃福展': True,'黄善聪': True,'陆用炯': True,'邓深华': True,'何迎年': True,'杨帆': True,'莫国珩': True,'蒙炳松': True}
                dcidlist = []
                for z in range(len(yun['data']['list'])):
                    result = name.get(yun['data']['list'][z]['OperName'])
                    if result == True:
                        dcidlist.append(yun['data']['list'][z]['partake']['AP_ID'])
                for x in dcidlist:
                    xa = s.post(url='http://gxic.itolearn.com/webios/Result',data={'apIdList': x, 'icAID': list['items'][b]['ID'], 'type': 1})
                    print(xa.status_code)
                    xb = s.post(url='http://gxic.itolearn.com/HomeNote/InsertNoteHome', data={'AP_ID': x, type: 3})
                    print(xb.status_code)
            if list['items'][b]['typeId'] == '5':
                name = {'覃福展': True,'黄善聪': True,'陆用炯': True,'邓深华': True,'何迎年': True,'杨帆': True,'莫国珩': True,'蒙炳松': True}
                dcidlist = []
                if list['items'][b]['StuSubmitStatus'] == 0:
                    # o=s.post('http://gxic.itolearn.com/Weixin/getmaterial',data=postjk)
                    postjk={"courseElementId":str(list['items'][0]['courseElmentId'])}
                    o = s.get('http://gxic.itolearn.com/Weixin/material', params=postjk)
                    print(o.text)
                    postdata2 = {
                        "id": list['items'][0]['courseElmentId'],
                        "content": "已阅读",
                        "Type": 2
                    }
                    jr = s.post(
                        'http://gxic.itolearn.com/webios/addComment', data=postdata2)
                    print(jr.status_code, jr.text)
                for c in range(1, 6):
                    # postjk={"courseElementId":str(json.loads(cr.text)['items'][0]['courseElmentId'])}
                    # postjk.update(headere)
                    # print(postjk)
                    par = {
                        'id': list['items'][b]['courseElmentId'],
                        'page': c,
                        'pageSize': 10
                    }
                    i = s.get(
                        'http://gxic.itolearn.com/Weixin/getDiscussionContent', params=par)
                    try:
                        for d in range(10):
                            result = name.get(json.loads(i.text)[
                                              'list'][d]['OperName'])
                            if result == True:
                                dcidlist.append(json.loads(i.text)[
                                                'list'][d]['DiscussionContent']['DC_ID'])
                    except:
                        pass
                for e in dcidlist:
                    ll = {'dcid': e, 'ica_type': 5, 'type': 1}
                    des = s.post(
                        'http://gxic.itolearn.com/webios/addAppreciation', data=ll)