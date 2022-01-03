"""
作者：Big_hunzi
日期：2021年11月01日   16:55

主题：获取字典视图
"""

scores={'张三':100,'李四':98,'王五':45}

#获取所有的键
keys=scores.keys()
print(keys,type(keys))
print(list(keys))#将所有键组成的视图转成列表

#获取所有的值
values=scores.values()
print(values,type(values))

#获取所有的键值对
items=scores.items()
print(items,type(items))
print(list(items))#转换之后的列表元素是由元组组成