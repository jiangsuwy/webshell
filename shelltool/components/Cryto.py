# -*- encoding: utf-8 -*-
"""
@File    :   Cryto.py
@Modify Time          @Author      @Version    
------------        -----------    --------    
2021/3/8 22:41      flandre2333      1.0

@Description
-----------

"""
from Crypto.Cipher import AES
import base64


class Base64Crypt:
    @staticmethod
    def Base64Encode(plaintext, encoding='utf8'):
        return base64.encodebytes(plaintext.encode(encoding)).decode()

    @staticmethod
    def Base64Decode(ciphertext, encoding='utf8'):
        return base64.b64decode(ciphertext).decode()


class AESCrypt:
    """
    AES/CBC/PKCS5Padding 加密
    """

    def __init__(self, key):
        if len(key) != 16:
            raise RuntimeError("密钥长度不是16位!!!")
        self.key = key.encode()
        self.vi = bytes(16)
        self.Mode = AES.MODE_CBC
        self.block_size = 16
        self.padding = lambda data: data + ((self.block_size - len(data.encode('utf-8')) %
                                             self.block_size) * chr(
            self.block_size - len(data.encode('utf-8')) % self.block_size))
        self.unpadding = lambda data: data[:-ord(data[-1])]

    def aes_encrypt(self, plaintext=str) -> str:
        """
        AES 加密
        :param plaintext: 明文字符串
        :return:
        """
        # * 将密文补充为16位,并转为字节
        aes_plain = self.padding(plaintext).encode('utf-8')
        # * 初始话加密容器
        crypto = AES.new(self.key, self.Mode, self.vi)
        # * 进行AES加密
        encrypt_aes = crypto.encrypt(aes_plain)
        # * 进行BASE64转码
        encrypt_text = (base64.b64encode(encrypt_aes)).decode()
        return encrypt_text

    def aes_decrypt(self, ciphertext) -> str:
        """
        AES 解密
        :param ciphertext: 密文字符串
        :return {str} 明文
        """
        # * 初始话加密容器
        crypto = AES.new(self.key, self.Mode, self.vi)
        # * 进行BASE64转码
        plain_base64 = base64.b64decode(ciphertext)
        # * 解密明文
        decrypt_aes = crypto.decrypt(plain_base64)
        # * 截取
        decrypt_aes = self.unpadding(decrypt_aes.decode('utf-8'))
        return decrypt_aes
