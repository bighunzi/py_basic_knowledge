"""
作者：Big_hunzi
日期：2021年11月04日   11:49

主题：字符串的常用操作：大小写
"""

s='hello,python'
a=s.upper()#转成大写之后，会产生一个新的字符串对象
print(a,id(a))
print(s,id(s))
b=s.lower()
print(b,id(b))#虽然原来就是小写的，但是转换之后，依旧会产生一个新的字符串对象。
print(b==s,b is s)


s2='hello,Python'
print(s2.swapcase())#大写变小写，小写变大写

print(s2.capitalize())#第一个字符大写，其余均小写。
print(s2.title())#每个单词的第一个字符大写，其余均小写。