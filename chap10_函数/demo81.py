"""
作者：Big_hunzi
日期：2021年11月04日   22:06

主题：函数的返回值
"""

print(bool(0))
print(bool(8))

def fun(num):
    odd=[]#存奇数
    even=[]#存偶数
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even#返回了一个元组

lst=[10,29,34,58,68,57,83]
print(fun(lst))

'''
1、函数的返回值如果是1个，直接返回
2、函数的返回值如果是多个，返回的结果为元组
'''