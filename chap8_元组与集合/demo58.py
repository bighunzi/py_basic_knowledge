"""
作者：Big_hunzi
日期：2021年11月02日   11:56

主题：元组  t=('python','hello',90)
元组：python内置的数据结构之一，是一个不可变序列。
不可变序列:没有增删改操作。元组，字符串
可变序列：可以对序列进行增删改操作，对象地址不发生更改。列表，字典
"""

#可变序列
lst=[10,20,30]
print(id(lst))
lst.append(300)
print(lst,id(lst))

#不可变序列
s='hello'
print(s,id(s))
s=s+'world'
print(s,id(s))
