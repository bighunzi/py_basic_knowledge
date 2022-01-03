"""
作者：Big_hunzi
日期：2021年11月13日   16:23

主题：文件对象的常用方法

移动文件指针
"""
file=open('a.txt','r')
file.seek(2)#一个中文字符占两个字节，所以得写2
print(file.read())
print(file.tell())#输出的指针位置是在最后一个字母后面的空格位置上的。一个回车'\n'占用两个字节
file.close()