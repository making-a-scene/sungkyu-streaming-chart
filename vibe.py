from selenium import webdriver
from bs4 import BeautifulSoup
import time


def get_vibe_chart():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)

    url = "https://vibe.naver.com/chart/total"
    driver.get(url)
    time.sleep(3)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    items = soup.select('div.tracklist tr')

    chart_data = []
    for i, item in enumerate(items):
        title_el = item.select_one('td.song div.title_badge_wrap span.inner_cell a span')
        artist_el = item.select_one('td.song div.artist_sub span.artist_sub_inner span a span')
        if title_el and artist_el:
            chart_data.append({
                'rank': len(chart_data) + 1,
                'title': title_el.text.strip(),
                'artist': artist_el.text.strip()
            })
    return chart_data


def get_artist_rank(artist='김성규'):
    chart_data = get_vibe_chart()
    results = []
    for item in chart_data:
        if item['artist'] == artist:
            results.append(item)
    return {
        'chart_name': '바이브',
        # 'all_data': chart_data,
        'artist_ranks': results,
    }


if __name__ == "__main__":
    result = get_artist_rank()
    if result['artist_ranks']:
        for item in result['artist_ranks']:
            print(f"바이브 {item['rank']}위 - {item['title']}")
    else:
        print("바이브 -")
