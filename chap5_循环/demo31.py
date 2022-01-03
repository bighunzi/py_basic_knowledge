"""
作者：Big_hunzi
日期：2021年10月28日   12:45

主题：for-in 循环
in表达从（字符串，序列等）中依次取值，又称为遍历
for-in遍历的对象必须是可迭代对象

for 自定义的变量 in 可迭代对象：
"""

for item in 'Pyhthon':#第一次取出来的是P，将P赋值item，将item输出。第二次为y,以此类推。
    print(item)

#range()序列。也是一个可迭代对象
for i in range(10):
    print(i)

#如果循环体中不需要使用到自定义变量，可将自定义变量写为'_'
for _ in range(5):
    print('人生苦短，我用python')

#使用for循环计算1到100偶数和
sum=0

for i in range(0,101,2):
    sum+=i

print(sum)