"""
作者：Big_hunzi
日期：2021年10月23日   17:26

主题：浮点数
"""
a=3.14159
print(a,type(a))
n1=1.1
n2=2.2
n3=n1+n2
print(n1+n2) #浮点数存储不精确性
print(n1+n3)


from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))