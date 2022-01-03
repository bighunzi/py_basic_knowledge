"""
作者：Big_hunzi
日期：2021年10月29日   12:28

主题：获取指定元素的索引；获取列表中指定的元素
"""
lst=['hello','world',98,'hello']
print(lst.index('hello'))#只返回相同元素的第一个元素的索引
#print(lst.index('Python')) 'Python' is not in list 出现异常
print(lst.index('hello',1,4))#左闭右开

print(lst[0])
print(lst[-3])

