import requests


def get_flo_chart():
    req = requests.get('https://www.music-flo.com/api/display/v1/browser/chart/1/track/list?size=100')
    data = req.json()

    new_musics = data['data']['trackList']
    chart_data = []
    for i in range(len(new_musics)):
        chart_data.append({
            'rank': i + 1,
            'title': new_musics[i]['name'],
            'artist': new_musics[i]['artistList'][0]['name']
        })
    return chart_data


def get_artist_rank(artist='김성규'):
    chart_data = get_flo_chart()
    results = []
    for item in chart_data:
        if item['artist'] == artist:
            results.append(item)
    return {
        'chart_name': '플로',
        'all_data': chart_data,
        'artist_ranks': results,
    }


if __name__ == "__main__":
    result = get_artist_rank()
    if result['artist_ranks']:
        for item in result['artist_ranks']:
            print(f"플로 {item['rank']}위 - {item['title']}")
    else:
        print("플로 -")
