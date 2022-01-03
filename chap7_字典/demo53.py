"""
作者：Big_hunzi
日期：2021年11月01日   16:50

主题：字典的增删改操作
"""
#key的判断
scores={'张三':100,'李四':98,'王五':45}
print('张三' in scores)
print('张三' not in scores)

#删除
del scores['张三']#删除指定的key-value对
print(scores)

#scores.clear() #清空字典的元素
#print(scores)

scores['陈六']=98#新增元素
print(scores)

scores['陈六']=100#修改元素
print(scores)
