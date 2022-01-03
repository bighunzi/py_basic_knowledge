"""
作者：Big_hunzi
日期：2021年11月13日   20:08

主题：with语句（上下文管理器）

应用见demo113

with语句可以自动管理上下文资源，不论什么原因跳出with块，都能确保文件正确的关闭，以此来达到释放资源的目的。
"""
#with ……as中间的称为上下文表达式，它的结果是一个上下文管理器。

print(type(open('a.txt','r')))#所以以后建议with语句的方式
with open('a.txt','r') as file:#就不用写close了，因为它会自动释放资源
   print(file.read())

'''
MyContentMgr实现了特殊方法_enter_(),_exit_()。这个类对象遵守了上下文管理器协议
该类对象的实例对象，称为上下文管理器。

'''
class MyContentMgr:
    def __enter__(self):
        print('enter方法被调用执行了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用执行了')

    def show(self):
        print('show方法被调用执行了',1/0)#可以看到，纵使show()出错，enter,exit，同样被调用

with MyContentMgr() as file:
    file.show()