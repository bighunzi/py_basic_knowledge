"""
作者：Big_hunzi
日期：2021年11月03日   12:45

主题：集合的数学操作
"""

s1={10,20,30}
s2={20,30,40}

print(s1.intersection(s2))#交集
print(s1 & s2)#与上面等价

print(s1.union(s2))#并集
print(s1 | s2)

print(s1,s2)

print(s1.difference(s2))#差集
print(s1-s2)

print(s1.symmetric_difference(s2))#对称差集
print(s1^s2)