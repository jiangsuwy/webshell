# -*- encoding: utf-8 -*-
"""
@File    :   ReadFileTest.py    
@Modify Time          @Author      @Version    
------------        -----------    --------    
2021/3/9 12:47      flandre2333      1.0         

@Description
-----------
   None
"""
from components.ReadFile import ReadFile

FILENAME = '/payload/Cmd.php'
File = ReadFile(FILENAME)
print(File)
test = "flandre"
string = 'asdfasd{0}'.format(test)
print(string)
