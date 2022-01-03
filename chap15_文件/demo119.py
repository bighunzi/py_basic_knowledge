"""
作者：Big_hunzi
日期：2021年11月13日   20:28

主题：os模块的常用函数

os模块是Python内置的与操作系统功能和文件系统相关的模块，该模块中的语句的执行结果通常与操作系统有关，在不同的操作系统上运行，得到的结果可能不一样。
os模块与os.path模块用于对目录或文件进行操作。
"""
#os模块可以调用系统文件
import os
#os.system('notepad.exe')

#直接调用可执行文件
#os.startfile('C:\\Tencent\\QQ\\Bin\\qq.exe')#转义字符要加两个斜线

print(os.getcwd())#返回当前的工作目录
lst=os.listdir('../chap15_文件')#返回指定路径下的文件和目录信息   ../是退到上级目录
print(lst)

os.mkdir('newdir')#创建目录
#os.makedirs('A/B/C')#创建多级目录
#os.rmdir('newdir')#删除目录
#os.removedirs('A/B/C')

os.chdir('D:\\pythonProject\\vippython\\chap15_文件')#将path设置为当前工作目录
print(os.getcwd())#返回当前的工作目录