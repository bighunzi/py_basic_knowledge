"""
作者：Big_hunzi
日期：2021年11月05日   22:05

主题：斐波那契数列
"""
def fbnq(n):
    if n==1 or n==2:
        return 1
    else:
        return fbnq(n-1)+fbnq(n-2)


print(fbnq(6))

#输出这个数列的前6位上的数字
for i in range(1,7):
    print(fbnq(i))
