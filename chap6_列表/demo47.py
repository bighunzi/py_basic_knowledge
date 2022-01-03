"""
作者：Big_hunzi
日期：2021年10月30日   15:13

主题：列表元素的删除操作
"""

#一次移除一个元素

lst=[10,20,30,40,50,60,70]
lst.remove(30)#如果有重复元素只移除第一个元素
print(lst)

#删除一个指定索引位置上的元素
lst.pop(1)
print(lst)

lst.pop()#默认移除最后一个元素
print(lst)

#切片
newlst=lst[1:3]
print(newlst)

#不产生新的列表对象
lst[1:3]=[]
print(lst)

#clear清楚列表中的所有元素
lst.clear()
print(lst)

#del 将列表对象删除
del lst
#print(lst)
