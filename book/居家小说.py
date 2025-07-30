import requests
from bs4 import BeautifulSoup
import time
from tqdm import tqdm

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}

def get(url, pbar, info):
    # 只在真正开始抓取时打印一次
    tqdm.write(f"正在爬取：{info}")
    try:
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        content = soup.find('div', id='chaptercontent')
        title = soup.find('span', class_='title').get_text(strip=True)
        text = content.get_text(separator='\n', strip=True)
        if len(text) > 60:
            with open(f'{title}.txt', 'w', encoding='utf-8') as f:
                f.write(text)
    except Exception as e:
        pass
    finally:
        pbar.update(1)
        time.sleep(0.2)

base_url = "https://fe68c1592abb7b99132c24.577ff.cfd/book/40684"
total = 500 * 4   # 500 章 × 4 个链接
with tqdm(total=total, desc="下载进度", unit="章") as pbar:
    for i in range(1, 501):
        get(f"{base_url}/{i}.html", pbar, f"第{i}章-主")
        for j in range(2, 5):
            get(f"{base_url}/{i}_{j}.html", pbar, f"第{i}章-分{j}")

