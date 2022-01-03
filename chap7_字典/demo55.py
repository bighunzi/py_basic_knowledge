"""
作者：Big_hunzi
日期：2021年11月01日   17:02

主题：字典元素的遍历
"""

scores={'张三':100,'李四':98,'王五':45}
for item in scores:
    print(item,scores[item],scores.get(item))