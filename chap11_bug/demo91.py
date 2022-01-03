"""
作者：Big_hunzi
日期：2021年11月07日   14:49

主题：traceback模块，使用其打印异常信息
"""
import traceback
try:
    print('----------------------------------------------------------------')#横线时而在前，时而在后。后面要讲的线程问题
    print(1/0)

except:
    traceback.print_exc()