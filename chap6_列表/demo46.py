"""
作者：Big_hunzi
日期：2021年10月30日   14:58

主题：列表元素得添加操作
"""

lst1=[10,20,30,40]
print(lst1,id(lst1))
lst1.append(100)#在列表的末尾添加一个元素
print(lst1,id(lst1))

lst2=['hello','world']
lst1.append(lst2)#将lst2作为一个元素添加到列表的末尾
print(lst1)
lst1.extend(lst2)#在列表的末尾一次性添加多个元素
print(lst1)

#在任意位置上添加一个元素
lst1.insert(1,90)
print(lst1)

#在列表的任意位置至少添加一个元素  切片
lst3=[True,False,'hello']
lst1[1:]=lst3#输入起止点，然后替换。
print(lst1)

lst1[1:1]=lst3
print(lst1)