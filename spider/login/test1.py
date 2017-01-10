'''
    模拟登陆，发送登陆表单数据，获取cookie并存储
'''
import requests
from http import cookiejar

params = {'username':'Lxiao','password':'password'}

# r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php",params)
# print("cookie is set to: ")
# print(r.cookies.get_dict())
# print('------------------')
# print("Going to profile page...")
# r = requests.get("http://pythonscraping.com/pages/cookies/profile.php",cookies = r.cookies)
# print(r.text)

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
}

session = requests.session()
session.cookies = cookiejar.LWPCookieJar(filename='cookies.txt')

try:
    session.cookies.load()
    print('加载cookie成功')
except:
    print('加载cookie失败')
    session.post("http://pythonscraping.com/pages/cookies/welcome.php",params,headers=headers)

print("Going to profile page...")
r = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(r.text)
session.cookies.save()
