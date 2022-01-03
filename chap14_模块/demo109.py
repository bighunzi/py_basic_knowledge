"""
作者：Big_hunzi
日期：2021年11月11日   12:10

主题：Python中常用的内容模块

sys:与Python解释器及其环境操作相关的标准库
time:提供与时间相关的各种函数的标准库
os：提供了访问操作系统服务功能的标准库
calendar:提供与日期相关的各种函数的标准库
urllib:用于读取来自网上(服务器)的数据标准库
json:
re:
math:
decimal:
logging:
"""
import sys
print(sys.getsizeof(24))#获取对象所占内存大小
print(sys.getsizeof(True))
print(sys.getsizeof(False))

import time
print(time.time())
print(time.localtime(time.time()))#转换成具体时间

import urllib.request
print(urllib.request.urlopen('http://www.baidu.com').read())
