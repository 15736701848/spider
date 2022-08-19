import requests
from bs4 import BeautifulSoup as BP
import json
import re
def kaixin_beitian(wo):
   data_dict={
    "info":wo,
    "userid":"2a311c31-9881-446e-871a-a3aeeaa1c275",
    "xsrf":""
   }
   headers={
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Accept":"application/xml, text/xml, */*; q=0.01",
    "X-Requested-With":"XMLHttpRequest"
   }
   a=requests.post('http://operation.tuling123.com/api/product_exper/chat.jhtml',params=data_dict,headers=headers)
   m=(a.content).decode('utf8')
   soup=BP(m,'html.parser')
   h=soup.text
   print("牛逼的人工智障:",h)
   if "搜索" in wo:
    a=input('关键词:')
    niubi="http://www.sougo.com/s?w="+a
    repon=requests.get(niubi)
    repon.encoding='utf8'
    soup=BP(repon.text,"html.parser")
    print(soup.text)
print('主人你好,我是您忠实舔狗,很好兴陪您聊天')
while True:
  data=input('帅气逼人的主人：')
  kaixin_beitian(data)

  