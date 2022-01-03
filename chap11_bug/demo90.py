"""
作者：Big_hunzi
日期：2021年11月06日   19:48

主题：
try-except-else:如果try块中没有抛出异常，则执行else块，如果抛出异常，执行except块
try-except-else-finally：finally块无论是否发生异常都会被执行，能常用来释放try块中申请的资源
"""
try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))

except BaseException as e:#e:invalid literal for int() with base 10: 'a'
    print('出错了',e)

else:
    result = a / b
    print('计算结果为：',result)

finally:
    print('谢谢您的使用')