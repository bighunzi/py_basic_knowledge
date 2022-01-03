"""
作者：Big_hunzi
日期：2021年11月13日   16:23

主题：文件对象的常用方法

读
"""
file=open('a.txt','r')
#print(file.read(1))#中
#print(file.readline())#中国
#print(file.readlines())#['中国\n', '美丽']
file.close()