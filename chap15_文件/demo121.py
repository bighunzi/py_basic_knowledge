"""
作者：Big_hunzi
日期：2021年11月13日   21:07

主题：
要求：列出指定目录下的所有py文件
"""
import os
path=os.getcwd()
lst=os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)