# -*- encoding: utf-8 -*-

from common.Types import LanguageType


class ShellEntity:
    def __init__(self, url, ip, password, languageType: LanguageType, os=None, remarks=None, add_time=None):
        self.url = url
        self.ip = ip
        self.password = password
        self.languageType = languageType
        self.os = os
        self.remarks = remarks
        self.add_time = add_time
