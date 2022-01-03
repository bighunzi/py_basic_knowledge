"""
作者：Big_hunzi
日期：2021年11月01日   17:21

主题：字典生成式

内置函数zip()
用于将可迭代的对象作为参数，将对象中对应的元素打包成一个元组，然后返回由这些元组组成的列表
"""

items=['Fruits','Books','Others']
prices=[80,70,91]
lst=zip(items,prices)
print(lst,list(lst))

d={item:price for item,price in zip(items,prices)}
print(d)

d={item.upper():price for item,price in zip(items,prices)}#.upper()大写
print(d)



items=['Fruits','Books','Others']
prices=[80,70,91,80,50]

d={item:price for item,price in zip(items,prices)}
print(d)