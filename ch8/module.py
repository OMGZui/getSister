from datetime import datetime
now = datetime.now()
print(now)
timestamp = now.timestamp()
print(timestamp)
print(datetime.fromtimestamp(timestamp))


# hashlib
import hashlib
md5 = hashlib.md5()
md5.update('123456'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('123456'.encode('utf-8'))
print(sha1.hexdigest())

# urllib
from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))
