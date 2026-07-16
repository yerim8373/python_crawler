import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
os.makedirs('docs', exist_ok=True)
URL = "https://m.etnews.com/news/hot_content_list.html"
res = requests.get(URL)
soup = BeautifulSoup(res.text, 'html.parser')
section = soup.select_one("section.textthumb")
top = section.select('ul li strong a')[:10]
now = datetime.now().strftime('%Y-%m-%d')
with open('docs/index.md','w',encoding='utf-8') as f:
    f.write(f"# {now} 많이본뉴스\n\n")
    for i, a in enumerate(top, 1):
        title = a.text.strip()
        link = "https://m.etnews.com"+a['href']
        f.write(f"{i}. [{title}]({link})\n")