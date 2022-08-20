import time
import random
import  requests
import json
import hashlib
import jsonpath
def a():
 url ='https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
 headers={
    'Cookie': 'OUTFOX_SEARCH_USER_ID=79467041@10.108.160.102; JSESSIONID=aaaYcfsIiH6Eq9tgeJY4x; OUTFOX_SEARCH_USER_ID_NCOO=1993965922.0769746; ___rl__test__cookies=1641525568356',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
     "Referer": "http://fanyi.youdao.com/"

 }
 user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
 time_=str(int(time.time()*1000))
 ch=input("帅哥,别光顾着改bug呀😜,请先写出你看不懂的单词：")
 time_salt=time_+str(random.randint(0,9))
 a = "fanyideskweb" + ch + time_salt + "]BjuETDhU)zqSxf-=B#7m"
 sign=hashlib.md5(a.encode()).hexdigest()
 bv=hashlib.md5(user_agent.encode()).hexdigest()
 form_data = {
            "i": ch,  # 要被翻译的数据
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": time_salt,  # 以毫秒为单位的时间戳 + 随机数字
            "sign": sign,  # 未知的js加密后的数据
            "lts": time_,  # 以毫秒为单位的时间戳
            "bv": "4abf2733c66fbf953861095a23a839a8",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
 }
 re = requests.post(url,headers=headers,params=form_data)
 repons=re.json()
 res=jsonpath.jsonpath(repons,'$...tgt')[0]
 print(res)
while 1:
  a()
  