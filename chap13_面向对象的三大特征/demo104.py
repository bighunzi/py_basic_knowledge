"""
作者：Big_hunzi
日期：2021年11月09日   19:27

主题：_new_ _init_演示创建对象的过程
过程忘了可以去看图

特殊方法：
_new_():用于创建对象
_init_():对创建的对象进行初始化
"""

class Person(object):
    def __new__(cls, *args, **kwargs):#调用Person时，就将其传给了cls
        print('_new_被调用执行了，cls的id值为{0}'.format(id(cls)))
        obj=super().__new__(cls)#继承了object，调用其方法。
                                #说明了在new中创建的obj对象就是self,就是p1.
        print('创建的对象的id为：{0}'.format(id(obj)))
        return obj
    def __init__(self,name,age):
        print('_init_被调用了，self的id值为：{0}'.format(id(self)))
        self.name=name
        self.age=age

print('object这个类对象的id为：{0}'.format(id(object)))
print('Person这个类对象的id为：{0}'.format(id(Person)))

p1=Person('张三',20)#调用Person时，就将其传给了cls
print('p1这个Person类的实例对象的id：{0}'.format(id(p1)))

