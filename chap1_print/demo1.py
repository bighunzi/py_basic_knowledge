"""
作者：asus
日期：2021年10月23日
"""

# 可以输出数字
print(520)
print(98.5)

#可以输出字符串
print('helloworld')

#还可以输出含有运算符的表达式
print(3+1)


#将数据输出到文件中，注意点：1.所指定的盘付存在。2.要使用file=fp
fp=open('D:/pythonProject/text.txt','a+')#a+ 如果文件不存在就创建，存在就在文件后继续追加
print('hello world',file=fp)
fp.close()


#不进行换行输出(输出内容再一行之中)
print('hello','world','Pyhon')