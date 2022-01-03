"""
作者：Big_hunzi
日期：2021年11月01日   17:12

主题：字典的特点
字典的key必须是不可变对象

字典可以根据需要动态地伸缩
字典会浪费较大的内存，是一种使用空间换时间的数据结构（可以去看本子上的示意图）
"""

d={'name':'张三','name':'李四'}#key不允许重复
print(d)


d={'name':'张三','nikename':'张三'}#value允许重复
print(d)

lst=[10,20,30]
#c={lst:100}#字典的key必须是不可变对象 TypeError: unhashable type: 'list'
