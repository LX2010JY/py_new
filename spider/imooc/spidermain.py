import os
from conf import COURSEURL,CHOOSE
from video_downloader import File_Downloader
import conf
from spider_mooc import HtmlParse,HtmlDownloader




class SpiderMain(object):
    def __init__(self):
        self.downloader = HtmlDownloader()
        self.parser = HtmlParse()

    def crawl(self,url):
        # 主页html
        html_cont = self.downloader.download(url)
        #主页视频数据
        self.res_datas = self.parser.parser(html_cont)

    def download(self,res_datas):
        # id 代表线程编号
        id = 0
        for res_data in res_datas:
            downloader = File_Downloader(res_data,id)
            id+=1
            conf.PERLIST.append(0)
            downloader.start()

    def cmdshow_gbk(self):
        print(u'################################################')
        print(u'慕课网视频下载')
        print(u'################################################')

        # try:
        ID = input('输入下载课程编号ID:')
        url = COURSEURL+str(ID)
        print(url)
        print(u'下载：',url)
        print(u'开始解析，请稍后.')
        self.crawl(url)
        conf.PERSUM - len(self.res_datas)*100.0
        print(u'共有{0}条视频'.format(len(self.res_datas)))
        print(u'课程名称：',self.res_datas[0].subject)
        for res_data in self.res_datas:
            print(u'------->',res_data.filename)
        state = input(u'选择清晰度（1：超清UHD，2：高清HD，3：普清SD）：')
        state = int(state)
        if state not in [1,2,3]:
            print(u'输入有误.')
            return
        conf.STATE = CHOOSE[state-1]
        self.download(self.res_datas)
        # except:
        #     print(u'程序炸了')
        #     return
