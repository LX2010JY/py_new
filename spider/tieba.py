import requests
import os
from bs4 import BeautifulSoup

url = "http://tieba.baidu.com/p/4178314700"

class Draw_tieba_pic:

    '''
        尝试以类的形式写爬虫
        输入爬取网页地址，和图片本地保存路径即可
    '''
    def __init__(self,url,dir):
        '''

        :param url: 爬取网站地址
        :param dir: 保存路径
        '''
        self.url = url
        self.dir = dir

    def check_save_dir(self,path=''):
        '''
        检查指定的保存路径是否存在，如果不存在，创建一个
        :return:
        '''
        diretor = self.dir
        if path!='':
            diretor += path

        if not os.path.exists(diretor):
            os.makedirs(diretor)

    def GetHtml(self):
        html = requests.get(self.url).text
        self.GetImg(html)



    def GetImg(self,html):
        '''
        通过网页html获取图片并下载
        :param html:
        :return:
        '''
        soup = BeautifulSoup(html,'html.parser')
        imglist = []
        for photourl in soup.find_all('img'):
            imglist.append(photourl.get('src'))
        x = 0
        for imgurl in imglist:
            print('download {0} --------->'.format(imgurl))
            try:
                self.check_save_dir()
                with open('{0}/{1}.jpg'.format(self.dir,x),'wb') as file:
                    file.write(requests.get(imgurl).content)
                    x+=1
            except:
                print('download {0} failed'.format(imgurl))

if __name__ == '__main__':
    dtp = Draw_tieba_pic("http://tieba.baidu.com/p/4865801796",'../file/秦时明月/')
    dtp.GetHtml()