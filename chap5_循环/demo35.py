"""
作者：Big_hunzi
日期：2021年10月28日   22:00

主题：流程控制语句 continue:用于结束当前循环，进入下一次循环

要求输出1到50之间所有5的倍数:使用continue实现
"""
'''
for item in range(1,51):
    if item%5==0:
        print(item)
'''


for item in range(1,51):
    if item%5!=0:
        continue
    print(item)
