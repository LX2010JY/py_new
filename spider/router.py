# -*-coding:utf-8-*-
import urllib,re
from urllib.request import urlopen
import os,sys
import requests
from bs4 import BeautifulSoup as soup

def get_ip_me(ip):
    a=[]
    # 这是一个将ip地址解析为地址的网址
    url = "http://www.ip138.com/ips138.asp?ip={0}&action2".format(ip)
    opurl = urlopen(url)
    c_data = opurl.read()
    c = soup(c_data,"html.parser")
    rdata = c.find_all("table",{"width":"80%"})
    data=c_data.decode('GBK')
    # 这里获取网页是GBK编码，但是存入ip.html的时候是以utf-8存入的，所以浏览器打开ip.html是以GBK解码的，所以会乱码
    with(open('../file/ip.html','w',encoding='utf-8')) as f:
        f.write(data)
    opurl.close()
    for x in rdata:
        x_l = ''.join(re.findall(u'本站主数据：(.*)',x.li.text))
        return '   %s  %s \n' % (ip,x_l)


def get_ip(ip):
    a = []
    url = "http://www.ip138.com/ips138.asp?ip={0}&action=2".format(ip)
    opurl = urlopen(url)
    o_data = opurl.read()
    opurl.close()
    c = soup(o_data,'html.parser')
    data = c.find_all("table", {"width": "80%"})
    for x in data:
        x_l = ''.join(re.findall(u'本站主数据：(.*)', x.li.text))
        return '    %s  %s \n' % (ip, x_l)



def get_tracert(domain):
    '''
    获取访问一个网址所经过的路由器
    还没看懂...
    :param domain:
    :return:
    '''
    ip_list = []
    data = os.popen('tracert -d %s ' % domain).readlines()
    b = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    data = [b.findall(x) for x in data]
    for x in data:
        if x != []:
            ip_list.append(''.join(x))
    return ip_list
if __name__ == '__main__':
    print('访问%s 经过的路由如下：\n' % sys.argv[1])
    for x in get_tracert(sys.argv[1]):
        print(get_ip(x))
