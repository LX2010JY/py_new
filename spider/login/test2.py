# coding:utf-8
'''
    http接入认证，就是test.lexue100.com需要登陆的那个东西
'''
import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('Lxiao','password')
r = requests.post(url="http://pythonscraping.com/pages/auth/login.php", auth=auth)
print(r.text)