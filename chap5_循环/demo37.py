"""
作者：Big_hunzi
日期：2021年10月28日   23:40

主题：else while
"""

a=0
while a<3:
    pwd=input('请输入密码：')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
    a+=1
else:
    print('对不起，三次密码均输入错误')