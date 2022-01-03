"""
作者：Big_hunzi
日期：2021年11月10日   11:55

主题：模块的导入

py中一个扩展名为.py的文件就是一个模块

使用模块的好处：
方便其他程序和脚本的导入并使用
避免函数名和变量名冲突
提高代码的可维护性
提高代码的可复用性
"""
import  math#关于数学运算的一个模块
print(id(math))
print(type(math))
print(math)
print(math.pi)
print('-------------------')
print(dir(math))
print(math.pow(2,3),type(math.pow(2,3)))#2的3次方
print(math.ceil(9.001))#向上取整
print(math.floor(9.99))

from math import pi
print(pi)

#调用自定义模块
import calc
print(calc.add(1,2))
print(calc.div(1,2))