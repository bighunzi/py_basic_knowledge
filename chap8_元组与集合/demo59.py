"""
作者：Big_hunzi
日期：2021年11月02日   12:03

主题：元组的创建方式
"""
#第一种
t=('python','world',90)
print(t,type(t))

#()可省略
t2='python','world',90
print(t2,type(t2))


#第二种  tuple()
t=tuple(('python','world',90))
print(t,type(t))

#只包含一个元组的元素需要使用逗号和小括号。
t=(10,)
print(t,type(t))#否则会认为成是本身的类型

#空元组的创建方式
t4=()
t5=tuple()
print(t4,type(t4),t5,type(t5))