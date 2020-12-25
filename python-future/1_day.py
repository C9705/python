# 接触爬虫的第一天，资源网站（阿里天池）https://developer.aliyun.com/lesson_1369_11724#_11724
# 通用爬虫：搜索引擎爬虫，无差别收集数据
# 聚焦爬虫；有针对性的编写特定领域，类别，主题的爬虫
# Robots协议：网站的根目录下面的文件，写明不同浏览器可以爬取哪些数据
# urllib包：
# import urllib
# 打开，读写url
from urllib.request import urlopen,Request
# urllib.request.urlopen(url, data=None, [timeout,]*, 
# cafile=None, capath=None, cadefault=False,context=None)
# 返回一个类文件对象
# web=urllib.request.urlopen('http://www.bing.com')#GET
# 查看是否关闭
# print(web.closed)
# User-Agent:获取网站的响应数据；伪装成某种浏览器
# 查看浏览器UA：navigator.userAgent（控制台操作）

ua="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
# 方式1
# req  = Request('http://www.bing.com',headers={'User-agent':ua})
req  = Request('http://www.mafengwo.cn/',headers={'User-agent':ua})
# 方式2
# reg.add_header('User-agent',ua)
web=urlopen(req)
with web: 
    print(1,type(web))
    print(2,web.status,web.reason)#状态
    print(3,web.geturl())#返回真正的URL
    print(4,web.info()) #返回headers
    print(5,web._method)#返回方式
    print(6,web.read()) #读取返回内容
print(web.closed)