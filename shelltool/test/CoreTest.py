# -*- encoding: utf-8 -*-
"""
@File    :   CoreTest.py    
@Modify Time          @Author      @Version    
------------        -----------    --------    
2021/3/9 13:35      flandre2333      1.0         

@Description
-----------
   None
"""
# from core.ShellEntity import ShellEntity
# from core.ShellService import ShellService
# from core.Types import LanguageType
# from components.Cryto import Base64Crypt

url = 'http://192.168.233.130/DVWA-master/hackable/uploads/shell1.php'
ip = url[url.find('//') + 2:url.find(',', url.find('//') + 2)]
print(ip)
# shellEntity = ShellEntity(url, ip, 'pass', LanguageType.PHP, os='win')
# useAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
# shellService = ShellService(shellEntity, useAgent)
# print(shellService.runCmd('dir')['msg'])
# print(shellService.runCmd('cd ../')['msg'])
# print(shellService.runCmd('dir')['msg'])

