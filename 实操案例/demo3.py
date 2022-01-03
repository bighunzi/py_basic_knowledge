"""
作者：Big_hunzi
日期：2021年11月18日   13:51

主题：
"""

pwd=input('支付密码：')
if pwd.isdigit():
    print('合法')
else:
    print('密码不合法，其只能是数字')


print('-------------------------')
s='支付密码合法' if pwd.isdigit() else '密码不合法，其只能是数字'
print(s)