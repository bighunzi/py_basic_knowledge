"""
作者：Big_hunzi
日期：2021年11月04日   17:54

主题：字符串的切片操作

字符串是不可变类型。
不具备增、删、改操作，切片操作将产生新的对象
"""
s='hello,Python'
s1=s[:5]
s2=s[6:]
s3='!'
new_str=s1+s3+s2
print(s1,s2)
print(new_str)

#一共有几个字符串参与运算
print(id(s),id(s1),id(s2),id(s3),id(new_str))


#[start,stop,step]
print(s[0:9:2])
print(s[::-1])
print(s[-6::1])