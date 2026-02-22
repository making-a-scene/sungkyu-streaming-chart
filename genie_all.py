import requests
from bs4 import BeautifulSoup
import time


def get_genie_chart():
    chart_data = []
    for i in range(1, 5):
        url = f'https://www.genie.co.kr/chart/top200?ditc=D&rtm=Y&pg={i}'
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        request = requests.get(url, headers=header)
        soup = BeautifulSoup(request.text, 'html.parser')
        table = soup.find('table', {'class': 'list-wrap'})
        titles = table.find_all('a', {'class': 'title ellipsis'})
        artists = table.find_all('a', {'class': 'artist ellipsis'})

        for j in range(len(titles)):
            title = titles[j].text.strip()
            artist = artists[j].text.strip()
            chart_data.append({
                'rank': (i - 1) * 50 + j + 1,
                'title': title,
                'artist': artist
            })
        time.sleep(0.5)
    return chart_data


def get_artist_rank(artist='김성규'):
    chart_data = get_genie_chart()
    results = []
    for item in chart_data:
        if item['artist'] == artist:
            results.append(item)
    return {
        'chart_name': '지니 TOP 200',
        # 'all_data': chart_data,
        'artist_ranks': results,
    }


if __name__ == "__main__":
    result = get_artist_rank()
    if result['artist_ranks']:
        for item in result['artist_ranks']:
            print(f"지니 TOP 200 {item['rank']}위 - {item['title']}")
    else:
        print("지니 TOP 200 -")
