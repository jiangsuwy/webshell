# -*- encoding: utf-8 -*-

import requests
from common import Types
from utils.GetDate import GetData
from utils.ReadFileGetData import ReadFileGetData


class RequestUtils:
    @staticmethod
    def sendRequest(url: str, headers: dict = None, method='get', data=None, isUseProxies=False,
                    proxies: dict = None) -> requests.models.Response:#封装的get方法
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
    def parseResponse(response: requests.models.Response, field: Types.ResponseField, **kwargs):#获取前期的get请求的cookie和key
        if field is Types.ResponseField.statusCode:
            return response.status_code  #获取状态码
        if field is Types.ResponseField.cookie:
            if kwargs['cookieToStr']:
                return str(response.cookies.get_dict())[1:-1].replace('\'', '').replace(': ', '=').replace(', ', ';')
            else:
                return response.cookies.get_dict()#获取cookie的值
        if field is Types.ResponseField.body:
            if not kwargs.get('code'):
                kwargs['code'] = 'utf8'
            return response.content.decode(kwargs['code'])#获取key

    @staticmethod
    def parseResponse1(response: requests.models.Response, field: Types.ResponseField, **kwargs):#获取前期的get请求的cookie和key
        if field is Types.ResponseField.statusCode:
            return response.status_code  #获取状态码
        if field is Types.ResponseField.cookie:
            if kwargs['cookieToStr']:
                return str(response.cookies.get_dict())[1:-1].replace('\'', '').replace(': ', '=').replace(', ', ';')
            else:
                return response.cookies.get_dict()#获取cookie的值
        if field is Types.ResponseField.body:
            if not kwargs.get('code'):
                kwargs['code'] = 'utf8'
            return response.content.decode(kwargs['code'])#获取key


    @staticmethod
    def requestAndParse(key, claName, params, languageType: Types.LanguageType, url, headers,
                        isUseProxies=False,
                        proxies: dict = None,
                        method='post'):
        headers['User-Agent'] = ReadFileGetData.userAgent()
        data = GetData.getSendData(key, claName, params, languageType)
        resp = RequestUtils.sendRequest(url, headers, method, data, isUseProxies, proxies)
        if RequestUtils.parseResponse(resp, Types.ResponseField.statusCode) == 200:
            respData = RequestUtils.parseResponse(resp, Types.ResponseField.body)
            return GetData.getParseData(key, respData)
        if RequestUtils.parseResponse(resp, Types.ResponseField.statusCode) == 302:
            return dict({'status': "fail", 'msg': ''})
        if RequestUtils.parseResponse(resp, Types.ResponseField.statusCode) == 404:
            return dict({'status': "fail", 'msg': ''})
        if RequestUtils.parseResponse(resp, Types.ResponseField.statusCode) == 500:
            return dict({'status': "fail", 'msg': ''})

    @staticmethod
    def requestAndParse1(key, claName, params, languageType: Types.LanguageType, url, headers,
                            isUseProxies=False,
                            proxies: dict = None,
                            method='post'):
        headers[ 'User-Agent' ] = ReadFileGetData.userAgent()
        data = GetData.getSendData(key, claName, params, languageType)
        resp = RequestUtils.sendRequest(url, headers, method, data, isUseProxies, proxies)
        return resp