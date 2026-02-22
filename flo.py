import requests

req  = requests.get('https://www.music-flo.com/api/display/v1/browser/chart/1/track/list?size=100')
data = req.json()

new_musics = data['data']['trackList']
result = []

flag = False
for i in range(len(new_musics)):
    if new_musics[i]['artistList'][0]['name'] == '김성규':
        print(f"플로 {i + 1}위")
        flag = True
        break
if not flag:
    print("플로 -")
