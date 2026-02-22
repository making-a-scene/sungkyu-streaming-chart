import requests
from bs4 import BeautifulSoup

def get_melon_chart():
    # 멜론 실시간 차트 URL
    url = "https://www.melon.com/chart/hot100/index.htm?chartType=D100"

    # 봇 탐지 방지를 위한 User-Agent 설정
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        # 멜론 차트 데이터 구조 파싱
        songs = soup.select('.service_list_song tr.lst50, .service_list_song tr.lst100')  # 1~100위
        melon_chart = []
        for rank, song in enumerate(songs, 1):
            title = song.select_one('.rank01 span a').text
            artist = song.select_one('.rank02 span a').text

            melon_chart.append({
                'rank': rank,
                'title': title,
                'artist': artist
            })

        return melon_chart
    else:
        print("페이지를 불러오지 못했습니다.")
        return []

def get_artist_rank(artist='김성규'):
    chart_data = get_melon_chart()
    results = []
    for item in chart_data:
        if item['artist'] == artist:
            results.append(item)
    return {
        'chart_name': '멜론 HOT 100(100일)',
        'all_data': chart_data,
        'artist_ranks': results,
    }


if __name__ == "__main__":
    result = get_artist_rank()
    if result['artist_ranks']:
        for item in result['artist_ranks']:
            print(f"멜론 HOT 100(100일) {item['rank']}위 - {item['title']}")
    else:
        print("멜론 HOT 100(100일) -")
