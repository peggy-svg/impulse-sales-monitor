import datetime
import json
import pathlib
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
PATH = ROOT / 'data' / 'history.json'
URL = 'https://www.kmonstar.com.tw/products/%E6%87%89%E5%8B%9F-261129-xdinary-heroes-9th-mini-album-impulse-%E5%B0%88%E8%BC%AF%E7%99%BC%E8%A1%8C%E7%B4%80%E5%BF%B5%E8%A6%96%E8%A8%8A%E7%B0%BD%E5%90%8D%E6%9C%83.json'

def main():
    request = urllib.request.Request(URL, headers={'User-Agent': 'ImpulseSalesMonitor/1.0 (public product JSON; 15-minute interval)', 'Accept': 'application/json'})
    with urllib.request.urlopen(request, timeout=25) as response:
        data = json.load(response)
    if str(data.get('id')) != '73504521':
        raise ValueError('Unexpected product ID; refusing to record')
    total = data.get('total_sold')
    if isinstance(total, bool) or not isinstance(total, int) or total < 0:
        raise ValueError('Missing/invalid total_sold; refusing to record')
    rows = json.loads(PATH.read_text(encoding='utf-8')) if PATH.exists() else []
    rows.append({'timestamp': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'total_sold': total})
    PATH.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('Recorded', total)

if __name__ == '__main__':
    main()
