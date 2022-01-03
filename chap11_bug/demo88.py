"""
作者：Big_hunzi
日期：2021年11月06日   16:41

主题：bug的常见类型
"""

#思路不清导致的错误
#1、print
#2、注释掉
lst=[{'title':'肖申克的救赎','actors':['蒂姆','摩根']},
     {'title':'霸王别姬','actors':['张丰毅','张国荣']}]
name=input('请输入你要查询的演员：')
for item in lst:
    if name in item['actors']:
        print(name,'出演了',item['title'])

