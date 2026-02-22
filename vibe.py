from selenium import webdriver
from bs4 import BeautifulSoup
import time

# 1. 드라이버 설정 (경로 설정 필요)
options = webdriver.ChromeOptions()
options.add_argument('headless')  # 브라우저 창 숨기기
driver = webdriver.Chrome(options=options)

# 2. 바이브 차트 페이지 접속
url = "https://vibe.naver.com/chart/total"
driver.get(url)
time.sleep(3)  # 페이지 로딩 대기

# 3. 데이터 수집
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Top 100 목록 태그 찾기
items = soup.select('div.tracklist tr')

flag = False
for i, item in enumerate(items):
    title_el = item.select_one('td.song div.title_badge_wrap span.inner_cell a span')
    artist_el = item.select_one('td.song div.artist_sub span.artist_sub_inner span a span')
    if title_el and artist_el:
        title = title_el.text.strip()
        artist = artist_el.text.strip()
        if artist == '김성규':
            print(f"바이브 {i + 1}위")
            flag = True
            break
if not flag:
    print("바이브 -")
