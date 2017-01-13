'''
    使用 pip install python-memcached 下载扩展
'''
import memcache
mc = memcache.Client(['127.0.0.1:11211'])
print(mc.get('foo'))
mc.set('foo','bar')
value = mc.get('foo')
print(value)