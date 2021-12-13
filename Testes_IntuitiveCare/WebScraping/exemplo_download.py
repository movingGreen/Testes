import requests



url = 'https://www.facebook.com/favicon.ico'
r = requests.get(url, allow_redirects=True)


open('facebook.ico', 'wb').write(r.content)

headers=requests.head(url).headers
downloadable = 'attachment' in headers.get('Content-Disposition', '')

print(downloadable)

if url.find('/'):
    print(url.rsplit('/', 1)[1])