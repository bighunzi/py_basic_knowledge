"""
作者：Big_hunzi
日期：2021年11月01日   16:42

主题：字典元素的获取
"""

scores={'张三':100,'李四':98,'王五':45}

#第一种方式 ：[]
print(scores['张三'])
#print(scores['陈六'])#KeyError: '陈六'


#get()方法
print(scores.get('张三'))
print(scores.get('陈六'))#None
print(scores.get('陈六',99))#99是查找'麻七'所对的value不存在时，提供的一个默认值。