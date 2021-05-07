# -*- encoding: utf-8 -*-

import os

ProjectName = 'webshelltool'


def ReadFile(FileName: str) -> str:
    cur_path = os.path.abspath(os.path.dirname(__file__))
    root_path = cur_path[:cur_path.find(ProjectName)+len(ProjectName)]
    file_path = root_path+FileName.replace('/','\\')
    print(file_path)
    if not os.path.exists(file_path):
        pass
    with open(file_path, 'r', encoding='utf-8') as f:
        file = f.read()
    return file
