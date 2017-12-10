#! python2
#coding=utf-8
import sys,base64,os
img="D:/gitrepos/captcha-tensorflow/vcode/3257hq.png"
img=open(img,"rb").read()
img=base64.b64encode(img)
sh='curl -i -k -X POST \"https://dm-55.data.aliyun.com/rest/160601/ocr/ocr_english.json\"  -H \"Authorization:APPCODE 1cf203228a8f488ba3f7b19a1904fcc7\" --data \'{"inputs": [{"image": {"dataType": 50,"dataValue":'+'\"'+img+'\"'+'}}]}\' -H \"Content-Type:application/json; charset=UTF-8\"'

sh1='curl -i -X POST \"http://ocr.market.alicloudapi.com/aliyunapp/[userid]\"  -H \"Authorization:APPCODE 1cf203228a8f488ba3f7b19a1904fcc7\" --data \"cid=1\&content='+img+'\&ext=.png\" -H \"Content-Type:application/json; charset=UTF-8\"'

#print sh1
print sh
print os.system(sh)

