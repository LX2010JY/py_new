# -*-coding:utf-8-*-
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from FileInfo import FileInfo
import conf
import re

class HtmlDownloader(object):
    '''
        获取教程首页html代码
    '''
    def download(self,url):
        if url is None:
            return None
        request = Request(url)
        request.add_header('user-agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36')
        request.add_header('host','www.imooc.com')
        response = urlopen(request)
        if response.getcode()!=200:
            return None
        return response.read()

class HtmlParse(object):
    '''
        html 解析，从中提取视频信息
    '''
    def __init__(self):
        # 存放视频地址
        self.res_data = []
    def parser(self,html_cont):
        '''
        :param html_cont: html内容
        :return:
        '''
        if html_cont is None:
            return None
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        subject = soup.find('div',class_="hd").get_text()
        links = soup.find_all('a',class_='J-media-item')
        html_down = HtmlDownloader()
        for link in links:
            fileinfo = FileInfo()
            # strip() 去除字符串前后空字符
            fileinfo.subject = subject.strip()
            fileinfo.filename = link.get_text().strip().replace(':','_').replace("\r\n","").replace(u'开始学习',"").replace(' ','')
            fileinfo.mid = link['href'].split('/')[2]
            json = html_down.download(conf.DOWNLOAD_URL.format(fileinfo.mid)).decode('utf-8').replace('\/','/')
            dic_json = eval(json)
            fileinfo.url['L'] = dic_json['data']['result']['mpath'][0]
            fileinfo.url['M'] = dic_json['data']['result']['mpath'][1]
            fileinfo.url['H'] = dic_json['data']['result']['mpath'][2]
            # 将
            self.res_data.append(fileinfo)

        return self.res_data






if __name__ == '__main__':
    html = HtmlDownloader()
    ret = html.download('http://www.imooc.com/learn/717')
    # with(open('../../file/mooc.html','w',encoding='utf-8')) as f:
    #     f.write(ret.decode('utf-8'))
    parser = HtmlParse()
    parser.parser(ret)


