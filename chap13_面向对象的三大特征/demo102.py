"""
作者：Big_hunzi
日期：2021年11月08日   21:54

主题：特殊方法和特殊属性
特殊属性：
_dict_:获得类对象或实例对象所绑定的所有属性和方法的字典

特殊方法：
_len_():通过重写_len_()方法，让内置函数len()的参数可以是自定义类型
_add_():通过重写_add_()方法,可使用自定义对象具有“+”功能
_new_():用于创建对象
_init_():对创建的对象进行初始化

"""
print(dir(object))#下划线开始和结束的 就是特殊方法    dir()可以查看对象的属性和方法

class A:
    pass
class B:
    pass

class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age

class D(A):
    pass


x=C('Jack',20) #x是C类型的一个实例对象
print(x.__dict__)#实例对象的属性字典
print(C.__dict__)#类对象的属性和方法


print('-----------------------------------')
print(x.__class__)#<class '__main__.C'>输出了对象所属的类
print(C.__bases__)#(<class '__main__.A'>, <class '__main__.B'>),输出的是C类的父类类型的元组
print(C.__base__)#输出的是前面第一个的父类
print(C.__mro__)#类的传递结构
print(A.__subclasses__())#子类的列表