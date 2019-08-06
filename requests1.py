
import datetime
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
url="https://www.fmkmk.com/"
req = Request(url)
try:
    response = urlopen(req)
except HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)
    f=open('Website_down_due_to_server_error.txt','wb')
    f.write(bytes('Website is not up and running because of the following reason',e.code,'utf-16'))

except URLError as e:
    print('We failed to reach a server.')
    print('Reason: ', e.reason)
    f1 = open('Website_down_due_to_url_error.txt', 'wb')
    f1.write(bytes('Website is not up and running because of the following reason','utf-16'))
else:
    print ('Website is working fine')
    f2 = open('Website_working.txt', 'wb')
    current_time=str(datetime.datetime.now())
    result=('Website is working fine on')
    f2.write(bytes(result,'utf-16'))