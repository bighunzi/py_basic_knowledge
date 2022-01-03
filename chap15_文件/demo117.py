"""
作者：Big_hunzi
日期：2021年11月13日   16:23

主题：文件对象的常用方法

缓冲区
Python-->缓冲区-->磁盘
"""
file=open('c.txt','a+')
file.write('hello')
file.flush()#有无此句的区别暂时不知道。
file.write('world')
file.close()