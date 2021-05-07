# -*- encoding: utf-8 -*-
"""
@File    :   ReadFile.py
@Modify Time          @Author      @Version    
------------        -----------    --------    
2021/3/9 12:44      flandre2333      1.0         

@Description
-----------
   None
"""
import os

ProjectName = 'shelltool'


def ReadFile(FileName: str) -> str:
    cur_path = os.path.abspath(os.path.dirname(__file__))#获取dir的路径
    print(cur_path)
    root_path = cur_path[:cur_path.find(ProjectName)+len(ProjectName)]#截取字符串
    print(root_path)
    file_path = root_path+FileName.replace('/','\\')#将/用\\来代替
    print(file_path)
    if not os.path.exists(file_path):#如果file_path路径不存在的话
        pass
    with open(file_path, 'r', encoding='utf-8') as f:
        file = f.read()
    return file#读取文件

file_a=ReadFile('/payload/Cmd.php')
print(file_a)