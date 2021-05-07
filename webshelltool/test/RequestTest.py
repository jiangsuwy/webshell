# -*- encoding: utf-8 -*-

from components.Request import RequestUtils
import requests
from components.Request import ResponseField
import random

requestHeader = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/88.0.4324.190 Safari/537.36',
}
url = 'http://192.168.233.130/DVWA-master/hackable/uploads/shells.php?pass=123'
resp = RequestUtils.sendRequest(url, isUseProxies=False)
print(RequestUtils.parseResponse(resp, ResponseField.statusCode))
cookie = RequestUtils.parseResponse(resp, ResponseField.cookie, key='PHPSESSID')
coookiedict = cookie.get_dict()
coookiedict['asdg']=123123
print(coookiedict)
print(str(coookiedict)[1:-1].replace('\'','').replace(': ','=').replace(', ',';'))
