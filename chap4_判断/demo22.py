"""
作者：Big_hunzi
日期：2021年10月26日   22:55

主题：单分支结构
"""
money=1000
s=int(input('请输入取款金额：'))

if money>=s:
    money=money-s
    print('取款成功，余额为：',money)


if money<s:
    print('余额不足')

