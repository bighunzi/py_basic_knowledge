"""
作者：Big_hunzi
日期：2021年10月29日   11:50

主题：二重循环中的break continue
"""

for i in range(5):
    for j in range(1,11):
        if j%2==0:
            continue#break
        print(j,end='\t')
    print()