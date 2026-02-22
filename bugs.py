import requests
from bs4 import BeautifulSoup


def get_bugs_chart():
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

        chart_data = []
        for i in range(len(titles)):
            title = titles[i].text.strip().split('\n')[0]
            artist = artists[i].text.strip().split('\n')[0]
            chart_data.append({
                'rank': i + 1,
                'title': title,
                'artist': artist
            })
        return chart_data
    else:
        print("페이지를 불러오지 못했습니다.")
        return []


def get_artist_rank(artist='김성규'):
    chart_data = get_bugs_chart()
    results = []
    for item in chart_data:
        if item['artist'] == artist:
            results.append(item)
    return {
        'chart_name': '벅스',
        'all_data': chart_data,
        'artist_ranks': results,
    }


if __name__ == "__main__":
    result = get_artist_rank()
    if result['artist_ranks']:
        for item in result['artist_ranks']:
            print(f"벅스 {item['rank']}위 - {item['title']}")
    else:
        print("벅스 -")
