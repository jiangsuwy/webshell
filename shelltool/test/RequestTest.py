# -*- encoding: utf-8 -*-
"""
@File    :   RequestTest.py
@Modify Time          @Author      @Version    
------------        -----------    --------    
2021/3/8 23:50      flandre2333      1.0         

@Description
-----------
   None
"""
from components.Request import RequestUtils
import requests
from components.Request import ResponseField
import random

requestHeader = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/88.0.4324.190 Safari/537.36',
}
url = 'http://192.168.217.130/DVWA/hackable/uploads/shells.php?pass=123'
resp = RequestUtils.SendRequest(url, isUseProxies=False)
print(resp.cookies.get_dict())
print(resp.content)
print(resp.text)
# print(RequestUtils.ParseResponse(resp, ResponseField.statusCode,cookieToStr=True))
cookie = RequestUtils.ParseResponse(resp, ResponseField.body)
print(cookie)
# coookiedict = cookie.get_dict()
# coookiedict['asdg']=123123
# print(coookiedict)
# print(str(coookiedict)[1:-1].replace('\'','').replace(': ','=').replace(', ',';'))

