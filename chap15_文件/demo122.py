"""
作者：Big_hunzi
日期：2021年11月13日   21:11

主题：遍历路径中所有路径和文件
"""
import os
path=os.getcwd()
lst_files=os.walk(path)
print(lst_files,type(lst_files))
for dirpath,dirname,filename in lst_files:
    print(dirpath)
    print(dirname)
    print(filename)
    print('-------------------')