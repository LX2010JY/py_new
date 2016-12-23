# 获取代理IP池
#coding:utf-8
import requests
import threading
import json
from bs4 import BeautifulSoup

class IProxy(object):
    def __init__(self):
        self.ipools = {}
        self.canuse_ips = {}
        self.timeout = 1

    def getHtml(self,url):
        '''
            获取网页内容
        :param url:
        :return:
        '''
        headers = {
            'User-Agent' : 'Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
        }
        res = requests.get(url,headers=headers)
        res.encoding = 'utf-8'
        return res.text


    def testIp(self):
        '''
            测试获取的代理ip是否可以访问
        :return:
        '''
        print('-'*20+'开始测试代理ip是否可用'+'-'*20)
        print('*'*20+'目前共有{0}条ip'.format(len(self.ipools))+'*'*20)
        url = "http://www.baidu.com"
        for ip in self.ipools:
            print('正在测试{0},访问www.baidu.com中...'.format(ip),end=' ')
            try:
                res = requests.get(url,proxies=self.ipools[ip],timeout=self.timeout)
                print('代理可用')
                self.canuse_ips[ip] = self.ipools[ip]
            except:
                print('连接超时，代理不可用')
        self.ipools.clear()
        self.ipools = self.canuse_ips
        print('-' * 20 + '测试完毕，目前共有{0}条ip可用'.format(len(self.canuse_ips)) + '-' * 20)

    def getProxy(self):
        '''
            获取所有网站的代理IP
        :return:
        '''
        self.GetProxyKuai()
        # self.GetProxyXici()
    def GetProxyKuai(self):
        '''
            从快代理网站上面获取ip
        :return:
        '''
        url = "http://www.kuaidaili.com/proxylist/{0}/"
        # url = "http://www.kuaidaili.com/free/inha/{0}/"
        for page in range(4,51):
            print('【快代理】正在从{0}获取免费代理IP'.format(url.format(page)))
            content = self.getHtml(url.format(page))
            with(open('../../file/kuai{0}'.format(page),'w',encoding='utf-8')) as f:
                f.write(content)
            BsObj = BeautifulSoup(content,"html.parser")
            tbody = BsObj.find('tbody')
            trs = tbody.find_all('tr')
            for tr in trs:
                ip = {}
                IP = tr.find('td',{'data-title':'IP'}).get_text()
                PORT = tr.find('td',{'data-title':'PORT'}).get_text()
                HTTP = tr.find('td',{'data-title':'类型'}).get_text()
                types = HTTP.split(',')
                for type in types:
                    ip[type.strip().lower()] = "http://{0}:{1}".format(IP,PORT)
                    self.ipools[IP] = ip
        print('-'*20+'【快代理】免费代理IP获取完毕'+'-'*20)

    def GetProxyXici(self):
        '''
            从西刺代理获取代理ip地址
        :return:
        '''

        url = "http://www.xicidaili.com/nt/{0}"
        for page in range(1,10):
            print('【西刺代理】正在从{0}获取免费代理IP'.format(url.format(page)))
            content = self.getHtml(url.format(page))
            BsObj = BeautifulSoup(content,"html.parser")
            trs = BsObj.findAll('tr',{"class":"odd"})
            for tr in trs:
                ip = {}
                tds = tr.findAll('td')
                IP = tds[1].get_text()
                PORT = tds[2].get_text()
                HTTP = tds[5].get_text()
                ip[HTTP.strip().lower()] = "http://{0}:{1}".format(IP,PORT)
                self.ipools[IP] = ip

        print('-' * 20 + '【西刺代理】免费代理IP获取完毕' + '-' * 20)
    def save(self):
        '''
            保存ip到文件
        :return:
        '''
        ipjsons = json.dumps(self.ipools)
        with(open('../../file/ip.json','w',encoding='utf-8')) as f:
            f.write(ipjsons)
    def showips(self):
        for ip in self.ipools:
            print(ip)
if __name__ == '__main__':
    pools = IProxy()
    # pools.GetProxyKuai()
    # pools.GetProxyXici()
    # pools.GetProxy66()
    pools.getProxy()
    pools.testIp()
    # pools.save()

