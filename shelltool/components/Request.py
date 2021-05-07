# -*- encoding: utf-8 -*-
"""
@File    :   Request.py
@Modify Time          @Author      @Version    
------------        -----------    --------    
2021/3/8 23:19      flandre2333      1.0         

@Description
-----------
   None
"""
import requests
from enum import Enum


class ResponseField(Enum):
    statusCode = 1
    cookie = 2
    body = 3


class RequestUtils:
    @staticmethod
    def SendRequest(url: str, headers: dict = None, method='get', data=None, isUseProxies=False,
                    proxies: dict = None) -> requests.models.Response:
        if headers is None:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                     'Chrome/88.0.4324.190 Safari/537.36', }
        if proxies is None:
            proxies = {'http': 'http://127.0.0.1:8080',
                       'https': 'https://127.0.0.1:8080'}
        else:
            pass
        if isUseProxies:
            response = requests.request(method=method, url=url, headers=headers, proxies=proxies, data=data)
        else:
            response = requests.request(method=method, url=url, headers=headers, data=data)

        return response

    @staticmethod
    def ParseResponse(response: requests.models.Response, field: ResponseField, **kwargs):
        if field is ResponseField.statusCode:
            return response.status_code
        if field is ResponseField.cookie:
            if kwargs['cookieToStr']:
                return str(response.cookies.get_dict())[1:-1].replace('\'', '').replace(': ', '=').replace(', ', ';')
            else:
                return response.cookies.get_dict()
        if field is ResponseField.body:
            if not kwargs.get('code'):
                kwargs['code'] = 'utf8'
            return response.content.decode(kwargs['code'])
