"""
作者：Big_hunzi
日期：2021年10月25日   16:52

主题：比较运算符
"""
a,b=10,20
print('a>b么？',a>b)
print('a<b么？',a<b)
print('a<=b么？',a<=b)
print('a=b么？',a==b)
print('a!=b么？',a!=b)

"""
==比较的是值，还是标识（内存地址）呢？
比较的是值。
比较对象的标识   使用is
"""


a=10
b=10
print(a==b)
print(a is b) #说明a与b的标识相等

lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1==lst2)
print(lst1 is lst2)
print(id(lst1),id(lst2))
print(a is not b)
print(lst1 is not lst2)