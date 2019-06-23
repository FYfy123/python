import requests
url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
response = requests.get(url)
HTML = response.text
URLS = HTML.split('\n')
# content = response.content
# print(content)
# if 'jpg' in url:
#     URLS.append(url)
for url in URLS:
    name = url.split('/')[-1].strip('\r')
    response = requests.get(url)
    content = response.content
    with open(name,'wb') as f:
        f.write(content)
        print(name)
    break