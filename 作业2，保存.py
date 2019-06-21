import urllib.request
import sys
reload(sys)
sys.setdefaultencoding('utf8')
html = request.get('http://www.17k.com/chapter/2933095/36699279.html')
open('q.text'.'w')as f:
   f.write(html.text)
data = urllib.parse.urlencode({'wd':'q'})
print(data)
url = 'http://www.baidu.com/s?' + data
response = urllib.request.urlopen(url)
HTML = response.read().decode('utf8')
print(HTML)
