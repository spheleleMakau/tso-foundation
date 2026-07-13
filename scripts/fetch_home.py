import urllib.request, urllib.error
url = 'http://127.0.0.1:8000/'
try:
    r = urllib.request.urlopen(url, timeout=10)
    print('STATUS', r.getcode())
    body = r.read().decode('utf-8', 'replace')
    print(body)
except urllib.error.HTTPError as e:
    print('HTTP ERROR', e.code)
    print(e.read().decode('utf-8', 'replace'))
except Exception as exc:
    print('ERROR', exc)
