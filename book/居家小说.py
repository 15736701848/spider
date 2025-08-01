import requests
from bs4 import BeautifulSoup
import time
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        }


text = " "


def build_url(chapter,part=None):
    '''
    构造url
    '''
    base = 'https://fe68c1592abb7b99132c24.577ff.cfd/book/40684'
    if part:
        return f'{base}/{chapter}_{part}.html'
    return f'{base}/{chapter}.html'



def dwnload_pages(url):
    '''
    获取主页及分页
    '''
    global text
    try:
        r1 = requests.get(url, headers=headers)
        soup1 = BeautifulSoup(r1.text, 'html.parser')
        content1 = soup1.find('div', id='chaptercontent')
        title1 = soup1.find('span', class_='title').get_text()
        text1 = content1.get_text(separator='\n', strip=True)
        if text1 in text:
            return None
        else:
            logging.info(f'正在下载{title1}...')
            text = text1
            with open(f'{title1}.txt', 'w', encoding='utf-8') as f:
                f.write(text1)

            time.sleep(1) #礼貌延时
            return 'ok'

    except Exception as e:
        logging.info(f'获取失败{e}')
        return 'Failed'




os.makedirs("斗罗大陆", exist_ok=True)
os.chdir("斗罗大陆")

for i in range(1, 501):
    dwnload_pages(build_url(i))
    for j in range(2, 5):
        statue = dwnload_pages(build_url(i,j))	
        if statue == None:
            break
