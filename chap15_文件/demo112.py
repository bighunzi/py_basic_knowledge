
"""
作者：Big_hunzi
日期：2021年11月12日   21:54

主题：文件的读写原理（可见图片）

文件的读写俗称'IO操作'
文件读写操作流程
操作原理
"""
file=open('a.txt','r')#打开或创建文件
print(file.readlines())#结果是一个列表
file.close()