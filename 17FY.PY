import urllib.request 
import urllib.parse
# data = urllib.parse.urlencode({'wd':'冰红茶'})
# print(data)
# url = 'http://www.baidu.com/s?' + data
# response = urllib.request.urlopen('http://www.baidu.com/s?' + data)
# HTML = response.read().decode('utf8')
# print(HTML)
#通过执行上面的语句，可以找到百度冰红茶相同的页面
data = bytes(urllib.parse.urlencode({'pw':'999','un':'mima'}),enconding='utf8')
url = 'http://httpbin.org/post'
response = urllib.request.urlopen(url,data=data)
result = response.read().decode('utf8')
print(result)