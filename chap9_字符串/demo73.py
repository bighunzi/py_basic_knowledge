"""
作者：Big_hunzi
日期：2021年11月04日   16:05

主题：字符串的的常用操作——替换与合并
"""
s='hello,Python,Python,Python'
#字符串替换
print(s.replace('Python','Java'))#默认全换
print(s.replace('Python','Java',2))#


#将列表或元组中的字符串合并成一个新字符串
lst=['hello','java','Python']
print('|'.join(lst))
print(''.join(lst))

t=('hello','java','Python')
print('|'.join(t))
print(''.join(t))


#如果对象是字符串
print('*'.join('Pyhton'))#将字符串视为字符串序列