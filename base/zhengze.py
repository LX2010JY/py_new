# -*- coding:utf-8 -*-
import requests
from urllib.request import urlopen,Request
import re
import codecs
url = "http://blog.sina.com.cn/u/1245336194"
headers = {
	'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0',
	'Accept-Language' : 'zh-CN,zh;q=0.8',
	'Cookie' : 'sso_info=v02m6alo5qztKWRk5ylkKSIpY6DjKWRk5ylkKSMpY6ToKadlqWkj5OEt46DoLGMs4C4jLOIwA==; SCF=Aq1NLl4uBLCyAl1_QpD_MVyR2Cf3UTRGC9ogwdy02h-jAr5a67crDa9XhVtRmpBtlaC148i5QSV_uhD5oKVI5Yw.; UOR=,,; SINAGLOBAL=221.221.148.148_1475917489.951688; vjuids=-59b495911.157a389aac4.0.b82f3599c2599; U_TRS1=0000008e.6bf960cc.57f8b6b3.a2fc3fdf; SGUID=1477559737812_7672176; _s_loginStatus=1788130832; acp_bb=1; LiRe=true; lxlrtst=1478857552_o; SUB=_2A251LcIKDeTxGedJ41oQ8y7EyD6IHXVWWrTCrDV_PUNbm9AKLRWlkW9YkDPm4uqPzXPzoMAySL27hXP_kQ..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW4WZjyTH6gV_1VJTUaDWeE5NHD95QpS0nReKe71heEWs4DqcjCi--Ni-iFiKn0i--Ni-ihiK.R; ALF=1510663642; Apache=114.249.229.207_1479127647.973114; ULV=1479127813074:13:4:1:114.249.229.207_1479127647.973114:1478240931120; SessionID=90jgegmdiptppmh6tdshd6n4g6; SINABLOGNUINFO=1788130832.6a94b610.jia6yu6; _s_loginuid=1788130832; U_TRS2=000000cf.87cb3016.5829b30d.deac9ee8; lxlrttp=1479037442; BLOG_TITLE=%E7%BB%83%E7%BC%98%E7%9A%84%E5%8D%9A%E5%AE%A2; vjlast=1479127816.1479127844.10'
}

request = Request(url,headers=headers)
html = urlopen(request).read()
print('获取成功，写入file/index.html------->')
with open("../file/index.html",'w',encoding='utf-8') as f:
	f.write(html.decode('utf-8'))
	f.close()

res = ''
with codecs.open("../file/index.html","r",encoding="utf-8") as f:
	res = f.read().encode("GBK",'ignore').decode("GBK")
	print(res)
	print(len(res))


req = Request('http://www.lexue100.com')
html = urlopen(req).read();
# 获取的网页内容中有特殊字符，解码后不能直接print ??????后面什么原因还是不太了解，好像是解码没有全部成功
response = html.decode('utf-8').encode('GBK','ignore').decode('GBK')
# print(response)
regx = re.compile("<div .+</div>")
all_div = re.findall(regx,response)
num = 0
for div in all_div:
	# num++不对
	num+=1
	print("{0:>4}:{1}".format(num,div))