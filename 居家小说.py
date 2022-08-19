import requests as req
from bs4 import BeautifulSoup as BP
from concurrent.futures import ThreadPoolExecutor as pool
headers={
  "User-Agent":"Mozilla"
}
url="https://m.qb5.tw/chapters_8227/"
reponse=req.get(url,timeout=20,headers=headers)
print(reponse)
soup=BP(reponse.text,"html.parser")
k=soup.select("[href]")
list=[i for i in range(104) if i>=6]
def a():
  for i in list:
    v=k[i]
    if v.get('href'):
      c=v.get('href')
      ab=req.get(c,timeout=30,headers=headers)
      print(ab)
      soup2=BP(ab.text,'html.parser')
      print(soup2.text)
with pool(5) as t:
   t.submit(a)