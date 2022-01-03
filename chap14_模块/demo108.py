"""
作者：Big_hunzi
日期：2021年11月11日   11:53

主题：Python中的包

包是一个分层次的目录结构，它将一组功能相近的模块组织在一个目录下。
作用：代码规范；避免模块名称冲突

包与目录的区别：
包含_init_.py文件的目录称为包
目录里通常不包含_init_.py文件
"""
#在这个demo中导入package

import package.Module_A as A
print(A.a)


#其他导入方式:
#使用import方式进行导入时，只能跟包名或者函数名
import package
import calc

#使用from   import可以导入包，模块，函数，变量
from package import Module_A
from package.Module_A import a
