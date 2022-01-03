"""
作者：Big_hunzi
日期：2021年11月08日   18:56

主题：继承及其实现方式

如果一个类没有继承任何类，则默认继承object
Python支持多继承:class C(A,B):
定义子类时，必须在其构造函数中调用父类的构造函数
"""
class Person(object): #Person继承object类,object类是所有类的父类，如果没有定义继承哪个类，就继承object类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):#定义子类
    def __init__(self,name,age,stu_num):
        super().__init__(name,age)#使用super调用父类方法
        self.stu_num=stu_num

class Teacher(Person):
    def __init__(self,name,age,teachyear):
        super().__init__(name,age)
        self.teachyear=teachyear

stu=Student('张三','20','1001')
teacher=Teacher('李四',34,10)
stu.info()
teacher.info()