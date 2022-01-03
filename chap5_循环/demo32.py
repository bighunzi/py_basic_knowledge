"""
作者：Big_hunzi
日期：2021年10月28日   13:00

主题:输出100到999之间的水仙花数
举例：153=3**3+5**3+1**3
"""
for item in range(100,1000):#左闭右开
    ge=item%10
    shi=item%100//10
    bai=item//100
    if item==ge**3+shi**3+bai**3:
        print(item)
