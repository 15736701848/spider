import requests                                  
from bs4 import BeautifulSoup
import time
from tqdm import tqdm


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}

def get(url): 
    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text,'html.parser')              
        content = soup.find('div', id='chaptercontent')
        title = soup.find('span', class_='title').get_text()
        text = content.get_text(separator='\n', strip=True)
        if len(text)>60:
            print(f'正在下载{title}...')
            with open(f'{title}.txt','w')as t:
                t.write(text)
        time.sleep(1)
    except Exception as e:
        print(f'获取失败{e}')


for i in range(1,501):
    url = f'https://fe68c1592abb7b99132c24.577ff.cfd/book/40684/{i}.html'
    get(url)
    for j in tqdm(range(2,5),desc=f"子页面", leave=False):
        url = f'https://fe68c1592abb7b99132c24.577ff.cfd/book/40684/{i}_{j}.html'
        get(url)


