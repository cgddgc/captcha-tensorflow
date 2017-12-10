#! python2
#-*-coding:utf-8-*-
'''
import urllib, urllib.request, sys,base64


host = 'http://dm-55.data.aliyun.com'
path = '/rest/160601/ocr/ocr_english.json'
method = 'POST'
appcode = '1cf203228a8f488ba3f7b19a1904fcc7'
querys = ''
bodys = {}
url = host + path
img="D:/gitrepos/captcha-tensorflow/vcode/0.png"
img=open(img,"rb").read()
img=str(base64.b64encode(img),'utf-8')
#print(img)
bodys= "cid=1&content="+img+"&ext=.png"
#bodys=urllib.parse.urlencode(bodys).encode(encoding='UTF8')
#post_data={'cid':'1','content':img,'ext':'.png'}
post_data="\"inputs\": [{\"image\": {\"dataType\": 50,\"dataValue\": img}}]}"
#post_data=urllib.parse.urlencode(post_data).encode(encoding='UTF8')
request = urllib.request.Request(url, post_data)
print(post_data)
request.add_header('Authorization', 'APPCODE ' + appcode)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read()
if (content):
    print(content)
'''


import urllib, urllib2, sys,base64

img="D:/gitrepos/captcha-tensorflow/vcode/3257hq.png"
img=open(img,"rb").read()
img=base64.b64encode(img)
#img=str(img,'utf-8')
print img
url = 'http://dm-55.data.aliyun.com/rest/160601/ocr/ocr_english.json'
method = 'POST'
appcode = '1cf203228a8f488ba3f7b19a1904fcc7'
Querys = ''
Headers = ''
post_data = '{"inputs":{"image":{"dataType":50,"dataValue":img}}}'
#post_data = urllib.urlencode(post_data).encode('utf8')
#print post_data
request = urllib2.Request(url,post_data)
request.add_header('Authorization', 'APPCODE ' + appcode)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib2.urlopen(request)
content = response.read()
if (content):
    print content



'''

'''