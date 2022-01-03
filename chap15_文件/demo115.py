"""
作者：Big_hunzi
日期：2021年11月13日   19:32

主题：文件对象的常用方法

写
"""
file=open('c.txt','a')
#file.write('hello')
lst=['java','go','python']
file.writelines(lst)
file.close()