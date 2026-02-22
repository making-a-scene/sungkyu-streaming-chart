import os
import json
from datetime import datetime

DOWNLOAD_DIR = os.path.expanduser('~/Downloads')

import melon_all
import melon_30
import melon_100
import genie_all
import bugs
import flo
import vibe

CRAWLERS = [
    ('멜론 TOP 100', melon_all),
    ('멜론 HOT 100(30일)', melon_30),
    ('멜론 HOT 100(100일)', melon_100),
    ('지니 TOP 200', genie_all),
    ('벅스', bugs),
    ('플로', flo),
    ('바이브', vibe),
]

def crawl_all(artist='김성규'):
    results = []
    for chart_name, module in CRAWLERS:
        print(f"[크롤링 중] {chart_name}...")
        try:
            result = module.get_artist_rank(artist)
            results.append(result)

            if result['artist_ranks']:
                for item in result['artist_ranks']:
                    print(f"  -> {result['chart_name']} {item['rank']}위 - {item['title']}")
            else:
                print(f"  -> {result['chart_name']} -")
        except Exception as e:
            print(f"  -> {chart_name} 크롤링 실패: {e}")
            results.append({
                'chart_name': chart_name,
                'all_data': [],
                'artist_ranks': [],
            })
    return results


def export_to_json(results, filename=None):
    if filename is None:
        today = datetime.now().strftime('%Y%m%d_%H')
        filename = os.path.join(DOWNLOAD_DIR, f'chart_{today}.json')

    data = {
        'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'charts': results,
    }

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\nJSON 파일 저장 완료: {filename}")
    return filename


if __name__ == "__main__":
    print("=" * 50)
    print(f" 스트리밍 차트 크롤링 ({datetime.now().strftime('%Y-%m-%d %H:%M')})")
    print("=" * 50)

    results = crawl_all()

    print("\n" + "=" * 50)
    print(" JSON 파일로 저장 중...")
    print("=" * 50)

    export_to_json(results)
