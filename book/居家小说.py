import requests
from bs4 import BeautifulSoup
import time
from tqdm import tqdm

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}

def need_save(url):
    """返回是否需要保存及标题、正文"""
    try:
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        content = soup.find('div', id='chaptercontent')
        title = soup.find('span', class_='title').get_text(strip=True)
        text = content.get_text(separator='\n', strip=True)
        return len(text) > 60, title, text
    except Exception:
        return False, None, None

base_url = "https://fe68c1592abb7b99132c24.577ff.cfd/book/40684"
tasks = [(i, flag) for i in range(1, 501) for flag in [''] + [f'_{j}' for j in range(2, 5)]]

saved_cnt = 0           # 已保存的章节计数
pbar = tqdm(total=None, desc="保存进度", unit="章")  # 未知总长

for i, flag in tasks:
    url = f"{base_url}/{i}{flag}.html"
    ok, title, text = need_save(url)
    if ok:
        tqdm.write(f"正在爬取：第{i}章{flag or ''}")
        with open(f"{title}.txt", "w", encoding="utf-8") as f:
            f.write(text)
        saved_cnt += 1
        pbar.total = saved_cnt + (len(tasks) - pbar.n - 1)  # 动态估算（可选）
        pbar.update(1)
    time.sleep(0.2)

pbar.close()
print(f"\n全部完成，共保存 {saved_cnt} 章")

