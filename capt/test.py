import urllib.request
imgpath="D:/gitrepos/captcha-tensorflow/vcode/"
url = "https://jwxt.jnu.edu.cn/ValidateCode.aspx"


for i in range(100):
    fname=imgpath+str(i)+".png"
    print(fname)
    req=urllib.request.Request(url)
    req.addheaders=[('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0')]
    result=urllib.request.urlopen(req)
    img=open(fname,'wb')
    img.write(result.read())
    img.close()

