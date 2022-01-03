"""
作者：Big_hunzi
日期：2021年10月28日   0:20

主题：while练习题 1到100之间的偶数和
"""


a=1
sum=0

while a<=100:
    if not bool(a%2):
        sum+=a#python 对缩进敏感，要注意，有可能报错
        a+=1
    else:a+=1


print('1到100之间偶数和为',sum)

