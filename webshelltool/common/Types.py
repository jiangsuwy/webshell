# -*- encoding: utf-8 -*-
"""
@File    :   Types.py    
@Modify Time          @Author      @Version    
------------        -----------    --------    
2021/3/8 23:00      flandre2333      1.0         

@Description
-----------
   None
"""
from enum import Enum


class LanguageType(Enum):
    PHP = 1
    JAVA = 2
    ASP = 3
    ASPX = 4


class ResponseField(Enum):
    statusCode = 1
    cookie = 2
    body = 3


class RealCMDOperateType(Enum):
    CREATE = 1
    STOP = 2
    WRITE = 3
    READ = 4


class PlayLoadFileName(Enum):
    BasicInfo = 'BasicInfo'
    CMD = 'Cmd'
    ConnectBack = 'ConnectBack'
    Database = 'Database'
    Echo = 'Echo'
    FileOperation = 'FileOperation'
    RealCMD = 'RealCMD'
    SocksProxy = 'SocksProxy'
