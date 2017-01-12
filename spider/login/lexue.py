import requests
from http import cookiejar

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

session = requests.session()

session.cookies = cookiejar.LWPCookieJar('cookies')
try:
    session.cookies.load(ignore_discard=True)
    print("load cookies...")
except:
    params = {
        'username': '18811409281',
        'password': 'fjia6yu6',
        'keeplogin': 1,
        'identify': 'student',
        'isschool': 0,
        'seckey': '',
        'formhash': 'd1c98901',
        'login': 'ok'
    }
    r = session.post('http://www.lexue100.com/index.php?do=cp',params,headers=headers)
    session.cookies.save()
    if r.status_code == 200:
        print('login success')
    else:
        print('登录失败，请修改')

res = session.get('http://www.lexue100.com/student.php?do=index')
with(open('tmp.html','w',encoding='utf-8'))as f:
    f.write(res.text)
