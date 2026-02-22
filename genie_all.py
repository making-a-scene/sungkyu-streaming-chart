import requests
from bs4 import BeautifulSoup
import time

flag = False
for i in range(1, 5):
    url = f'https://www.genie.co.kr/chart/top200?ditc=D&rtm=Y&pg={i}'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    request = requests.get(url, headers=header)
    soup = BeautifulSoup(request.text, 'html.parser')
    table = soup.find('table', {'class':'list-wrap'})
    titles = table.find_all('a', {'class': 'title ellipsis'})
    artists = table.find_all('a', {'class': 'artist ellipsis'})

    for j in range(len(titles)):
        title = titles[j].text.strip()
        artist = artists[j].text.strip()
        if artist == '김성규':
            print(f"지니 TOP 200 {0:3d}위", (i - 1) * 50 + j + 1)
            flag = True
            break
    # 다음 페이지로 이동하기 전에 1초간 대기
    if not flag:
        time.sleep(0.5)
if not flag:
    print("지니 TOP 200 -")

