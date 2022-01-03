"""
作者：Big_hunzi
日期：2021年11月03日   21:40

主题：集合生成式
没有元组生成式
"""
#为什么？没有元组生成式
t=(i*i for i in range(10))
print(t)#试一下元组：<generator object <genexpr> at 0x000001EF7AA5EC80>

lst=[i*i for i in range(10)]
print(lst)
s={i*i for i in range(10)}
print(s)
