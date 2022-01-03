"""
作者：Big_hunzi
日期：2021年10月28日   23:32

主题：else
"""
for item in range(3):
    pwd=input('请输入密码：')
    if pwd=='888':
        print('密码正确')
        break
    else:
        print('密码不正确')
else:#当循环正常结束，没有结束break的时候才会执行
    print('对不起，三次密码输入均错误')
