#from time import *   调用time里的所有功能
#form time import time,localtime  只调用time的time() localtime()函数

import time as t
print(t.time())
print(t.gmtime)


#导入自己的模块

#放在同一目录下或者是在C:\Users\75286\AppData\Local\Programs\Python\Python37\Lib\site-packages


import MyModule
MyModule.Print('world')
