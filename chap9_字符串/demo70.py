"""
作者：Big_hunzi
日期：2021年11月04日   12:07

主题：字符串的常用操作：字符串对齐
"""
s='hello,Python'
print(s.center(20,'*'))#居中对齐:第一个参数指定宽度,第二个参数指定填充符，默认空格

print(s.ljust(20,'*'))

print(s.rjust(20,))

print(s.zfill(30))#右对齐，左边用0填充，只接收一个参数，用于指定字符串的宽度
print('-8910'.zfill(8))#-0008910  ？？