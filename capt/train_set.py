import urllib.request,time,os,random
from damatuWeb import DamatuApi
from PIL import Image
import numpy as np
from cfg.py import dmtusr,dmtpwd
class train_data():

    def __init__(self):
        pass

    def get_img(n):
        imgpath="D:/gitrepos/captcha-tensorflow/vcode/"
        url = "https://jwxt.jnu.edu.cn/ValidateCode.aspx"
        i=0
        while(i<=n):
            fname=imgpath+str(i)+".png"
            req=urllib.request.Request(url)
            req.addheaders=[('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0')]
            try:
                result=urllib.request.urlopen(req)
            except:
                print("timeout")
                time.sleep(5)
                result=urllib.request.urlopen(req)
            else:
                img=open(fname,'wb')
                img.write(result.read())
                img.close()
                print(fname)
                i+=1

    def ren(self,n,dmtusr,dmtpwd):
        dmt=DamatuApi(dmtusr,dmtpwd)
        path1="D:/gitrepos/captcha-tensorflow/test/"
        path2="D:/gitrepos/captcha-tensorflow/vcode/"
        err=0
        use=0
        for i in range(n):
            imgs=os.listdir(path2)
            f=random.choice(imgs)
            fname=path2+f
            print(fname)
            code=dmt.decode(fname,42)
            use+=1
            print(code)
            while(code=='ERROR' or str(code)[0:1]=='-'):
                err+=1
                code=dmt.decode(fname,42)
                use+=1
                #pass
            code=str(code)
            i+=1
            newname=path1+code+".png"
            c=1
            while(os.path.exists(newname)):
                newname=path1+code+str(c)+".png"
                c+=1
            print(i,newname)
            print("#######")
            os.rename(fname,newname)
        print("Total Request:"+str(use))
        print(i)
        print(err)

    def get_text_img(self,imgpath):
        imgs=os.listdir(imgpath)
        img=random.choice(imgs)
        code=img[0:4]
        fname=imgpath+img
        im=Image.open(fname)
        im=im.convert("RGB")
        
        #im.show()
        im=np.array(im)
        return code, im
if __name__=='__main__':
    td=train_data()
    #td.get_text_img()
    td.ren(500,dmtusr,dmtpwd)