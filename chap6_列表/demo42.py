"""
作者：Big_hunzi
日期：2021年10月29日   12:09

主题：列表对象的创建
"""
lst1=['hello','world',98]#可以混存，根据需要动态分配和回收内存
print(lst1)
print(lst1[-3])
print(lst1[0])
lst2=list(['hello','world',98])
print(lst2)


#差别
b=[1,2,3,4,5]
a=[b]
c=list(b)
print('a=',a)
print('c=',c)

