"""
作者：Big_hunzi
日期：2021年11月06日   17:20

主题：python的异常处理机制
python提供了异常处理机制，可以在异常出现时即时捕获，然后内部“消化”，让程序继续进行

多个except结构
捕获异常的顺序按照先子类后父类的顺序，为了避免遗漏可能出现的异常，可以在最后增加BaseException
"""

try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    result = a / b
    print('结果为', result)

except ZeroDivisionError:
    print('对不起，除数不允许为0')

except ValueError:
    print('对不起，只能输入数字')

print('程序结束')

