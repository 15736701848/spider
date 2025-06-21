import requests                                         from bs4 import BeautifulSoup
import time

headers = {                                                     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
        }

def get(url):
    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text,'html.parser')
        content = soup.find('div', id='chaptercontent')
        title = soup.find('span', class_='title').get_text()
        text = content.get_text(separator='\n', strip=True)
        if len(text)>60:                                            print(f'正在下载{title}...')
            with open(f'{title}.txt','w')as t:
                t.write(text)
        time.sleep(1)
    except Exception as e:
        print(f'获取失败{e}')


for i in range(200,501):
    url = f'https://m.a9eef.icu/index/21863/{i}.html'
    get(url)
    for j in range(2,5):
        url = f'https://m.a9eef.icu/index/21863/{i}_{j}.html'
        get(url)
