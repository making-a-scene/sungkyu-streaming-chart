import requests
from bs4 import BeautifulSoup

url = "https://music.bugs.co.kr/chart"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    titles = soup.select('p.title')
    artists = soup.select('p.artist')

    flag = False
    for i in range(len(titles)):
        title = titles[i].text.strip().split('\n')[0]
        artist = artists[i].text.strip().split('\n')[0]
        if artist == '김성규':
            print(f"벅스 {i + 1}위")
            flag = True
            break
    if not flag:
        print("벅스 -")
else:
    print("페이지를 불러오지 못했습니다.")