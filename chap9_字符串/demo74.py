"""
作者：Big_hunzi
日期：2021年11月04日   16:34

主题：字符串的比较操作
"""

#首先比较第一个字母，相同则后延
print('apple'>'app')
print('apple'>'banana')

#两字符比较时，比较的是其ordinal value(原始值)，
# 可以调用内置函数ord得到这个值。
# 与ord对应的是chr，可以调用chr：指定ordinal value得到其对应字符

print(ord('a'),ord('b'))
print(ord('杨'))

print(chr(98),chr(99))
print(chr(26473))

#==比对value。
# is 比对id
a=b='Python'
c='Python'
print(a==b)
print(b==c)

print(a is b)
print(b is c)