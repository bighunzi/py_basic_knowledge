"""
作者：Big_hunzi
日期：2021年11月08日   19:13

主题：方法重写
如果子类对继承自父类的某个属性或方法不满意，可以在子类中对其（方法体）进行重新编写，
子类重写后的方法中可以通过super().xxx()调用父类中被重写的方法。
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
    def info(self):#方法重写
        super().info()
        print('学号',self.stu_num)

class Teacher(Person):
    def __init__(self,name,age,teachyear):
        super().__init__(name,age)
        self.teachyear=teachyear
    def info(self):
        super().info()
        print('教龄',self.teachyear)

stu=Student('张三','20','1001')
teacher=Teacher('李四',34,10)
stu.info()
print('------------------------------------------------')
teacher.info()