# -*- encoding: utf-8 -*-

from components.ReadFile import ReadFile

FILENAME = '/playload/Cmd.php'
File = ReadFile(FILENAME)
print(File)
test = "flandre"
string = 'asdfasd{0}'.format(test)
print(string)
