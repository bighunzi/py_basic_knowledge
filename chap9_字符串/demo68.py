"""
作者：Big_hunzi
日期：2021年11月03日   22:29

主题：字符串的查询操作
"""
s='hello,hello'
print(s.index('lo'))#3 第一组
print(s.find('lo'))
print(s.rindex('lo'))#9 查找的是最后一组substr
print(s.rfind('lo'))


#print(s.index('k'))#ValueError: substring not found
print(s.find('k'))#不存在，返回-1
#print(s.rindex('k'))
print(s.rfind('k'))