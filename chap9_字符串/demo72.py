"""
作者：Big_hunzi
日期：2021年11月04日   12:32

主题：字符串的常用操作：字符串判断的相关方法
"""

#判断指定的字符串是不是合法的标识符
s='hello,python'
print('1',s.isidentifier())#False 合法的标识符是：字母、数字、下划线
print('2','hello'.isidentifier())
print('3','张三'.isidentifier())

#判断字符串是否全部由空白字符组成（回车、换行、水平制表符）
print('\t',1)
print(4,'\t'.isspace())
print(5,'\n'.isspace())
print(6,'\r'.isspace())

#判断是否全部由字母组成
print(7,'abc'.isalpha())
print(8,'张三'.isalpha())
print(9,'张三1'.isalpha())

#是否全部由十进制数字组成
print(10,'123'.isdecimal())
print(11,'123四'.isdecimal())#False
print(12,'ⅠⅤ'.isdecimal())#False

#是否全部由数字组成
print(13,'123'.isnumeric())
print(14,'123四'.isnumeric())#True
print(15,'ⅠⅤ'.isnumeric())#True

#是否全部由字母和数字组成
print(16,'abc1'.isalnum())
