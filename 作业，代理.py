import urllib.request
url = 'http://www.baidu.com'
proxy_handler = urllib.request.ProxyHandler({
    'http':'http://119.114.120.243:808',
    'https':'https://221.229.18.204:808',
    'https':'https://183.185.25.152:9797',
})
opener = urllib.request.build_opener(proxy_handler)
reponse = opener.open(url)
print(reponse.read())

