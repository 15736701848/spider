import requests
from bs4 import BeautifulSoup
import time

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        }


text = " "



def spider(url):
    global text
    try:
        r1 = requests.get(url, headers=headers)
        soup1 = BeautifulSoup(r1.text, 'html.parser')
        content1 = soup1.find('div', id='chaptercontent')
        title1 = soup1.find('span', class_='title').get_text()
        text1 = content1.get_text(separator='\n', strip=True)
        if text1 in text:
            return 6
        else:
            print(f'正在下载{title1}...')
            text = text1
            with open(f'{title1}.txt', 'w') as t:
                t.write(text1)
            time.sleep(1)

    except Exception as e:
        print(f'获取失败{e}')



def get(url):
    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        content = soup.find('div', id='chaptercontent')
        title = soup.find('span', class_='title').get_text()
        global text
        text = content.get_text(separator='\n', strip=True)
        print(f'正在获取{title}')
        with open(f'{title}.txt', 'w') as t:
            t.write(text)
        time.sleep(1)
    except Exception as e:
        print(f'获取失败{e}')


for i in range(1, 501):
    url = f'https://fe68c1592abb7b99132c24.577ff.cfd/book/40684/{i}.html'
    get(url)
    for j in range(2, 5):
        url = f'https://fe68c1592abb7b99132c24.577ff.cfd/book/40684/{i}_{j}.html'  
        statue = spider(url)	
        if statue == 6:
            break


