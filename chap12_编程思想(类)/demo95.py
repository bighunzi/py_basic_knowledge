"""
作者：Big_hunzi
日期：2021年11月07日   16:18

主题：类属性——类方法——静态方法的使用方式
类属性：类中方法外的变量称为类属性，被该类的所有对象所共享
类方法：方法，使用类名直接访问的方法
静类方法：主法，
"""

class Student:#Student就是类名，由一个或多个类名组成，每个单词的首字母大写，其余小写。(这是规范，不这么写也不报错)
    native_place='吉林'#直接写在类里的变量，称为类属性

    def __init__(self,name,age):#初始化方法
        self.name=name#self.name称为实例属性，进行了一个赋值操作，将局部变量的name的值赋给了实例属性
        self.age=age

    def eat(self):#实例方法(类之内成为方法，类之外成为函数)
        print('学生在吃饭...')

    @staticmethod
    def method():#静态方法
        print('我是用了staticmethod进行修饰，所以我是静态方法')

    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')


#类属性的使用方式
print(Student.native_place)
stu1=Student('张三',20)
stu2=Student('李四',30)
print(stu1.native_place)
print(stu2.native_place)
Student.native_place='天津'
print(stu1.native_place)
print(stu2.native_place)

#类方法的使用方式
Student.cm()

#静态方法的使用方式
Student.method()