"""
作者：Big_hunzi
日期：2021年10月28日   21:47

主题：流程控制语句

for in/while:
if:break
"""


'''从键盘录入密码，最多录入三次，如果正确就结束循环'''
for item in range(3):
    pwd=input('请输入密码')
    if pwd=='8888':
        print('密码正确')
        break
    else:print('密码不正确')