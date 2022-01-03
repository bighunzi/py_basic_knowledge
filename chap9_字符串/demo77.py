"""
作者：Big_hunzi
日期：2021年11月04日   19:23

主题：字符串的编码与转换

A计算机：str在内存中以Unicode表示
编码——byte字节传输——解码
B计算机：显示


编码：将字符串转换为二进制数据(bytes)
解码：将bytes类型的数据转换为字符串类型
"""

s='天涯共此时'

#编码
print(s.encode(encoding='GBK'))#编码：encode  在GBK这种编码格式中一个中文占两个字节。b(byte)表示二进制
                               #b'\xcc\xec\xd1\xc4\xb9\xb2\xb4\xcb\xca\xb1'
print(s.encode(encoding='UTF-8'))#在UTF-8这种编码格式下，一个中文占三个字节

#解码
#byte代表的就是一个二进制数据（字节类型的数据）
byte=s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))