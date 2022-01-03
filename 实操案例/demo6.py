"""
作者：Big_hunzi
日期：2021年11月19日   11:07

主题：
"""
def calc(a,b,op):
    if op=='+':
        return a+b
    elif op =='-':
        return a-b
    elif op=='*':
        return a*b
    elif op=='/':
        if b!=0:
            return a/b
        else:
            return '除数不能为0'

print(calc(2,0,'/'))
