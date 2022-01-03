"""
作者：Big_hunzi
日期：2021年11月04日   12:22

主题：字符串的常用操作：劈分
"""
s='hello world Python'
lst=s.split()#从字符串的左边开始劈分，默认的劈分字符是空格字符串，返回的值都是一个列表
print(lst)

s1='hello|world|Python'
print(s1.split())
print(s1.split(sep='|'))#设置参数sep来设置劈分字符
print(s1.split(sep='|',maxsplit=1))#maxsplit参数指定最大劈分次数

#rsplit   从右侧开始，其余同上
print(s.rsplit())
print(s.rsplit('|'))
print(s1.rsplit(sep='|',maxsplit=1))