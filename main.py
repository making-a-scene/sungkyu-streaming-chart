import os
import json
from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9))

OUTPUT_DIR = os.environ.get('OUTPUT_DIR', os.path.expanduser('/Users/kimseungju/sungkyu-streaming/public/charts'))

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
                # 'all_data': [],
                'artist_ranks': [],
            })
    return results


def export_to_json(results, output_dir=None):
    if output_dir is None:
        output_dir = OUTPUT_DIR

    os.makedirs(output_dir, exist_ok=True)

    data = {
        'updated_at': datetime.now(KST).strftime('%Y-%m-%d %H:%M'),
        'charts': results,
    }

    # 타임스탬프 파일
    today = datetime.now(KST).strftime('%Y%m%d_%H')
    timestamped = os.path.join(output_dir, f'chart_{today}.json')
    with open(timestamped, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"\nJSON 파일 저장 완료: {timestamped}")

    # latest.json (항상 최신 데이터)
    latest = os.path.join(output_dir, 'latest.json')
    with open(latest, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"JSON 파일 저장 완료: {latest}")

    return timestamped


if __name__ == "__main__":
    print("=" * 50)
    print(f" 스트리밍 차트 크롤링 ({datetime.now(KST).strftime('%Y-%m-%d %H:%M')})")
    print("=" * 50)

    results = crawl_all()

    print("\n" + "=" * 50)
    print(" JSON 파일로 저장 중...")
    print("=" * 50)

    export_to_json(results)
