"""
作者：Big_hunzi
日期：2021年11月07日   15:15

主题：
面向过程：事物比较简单，可以用线性的思维去解决
面向对象：事物比较复杂，使用简单的线性思维无法解决
他们都是解决实际问题的一种方式
解决复杂问题，通过面向对象方式便于我们从宏观上把握事物之间复杂的关系、方便我们分析整个系统
具体到微观操作，仍然使用面向过程方式来解决。
"""
'''
类与对象
数据类型：
不同的数据类型属于不同的类，使用内置函数查看数据类型
对象：
100，85都是int类下包含的相似的不同个例，这就叫实例与对象
'''

#定义类.类的组成：类属性，实例方法，静态方法，类方法
class Student:#Student就是类名，由一个或多个类名组成，每个单词的首字母大写，其余小写。(这是规范，不这么写也不报错)
    native_place='吉林'#直接写在类里的变量，称为类属性

    def __init__(self,name,age):#初始化方法
        self.name=name#self.name称为实例属性，进行了一个赋值操作，将局部变量的name的值赋给了实例属性
        self.age=age

    def eat(self):#实例方法(类之内称为方法，类之外称为函数)
        print('学生在吃饭...')

    @staticmethod
    def method():#静态方法
        print('我是用了staticmethod进行修饰，所以我是静态方法')

    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')

print(id(Student))
print(type(Student))
print(Student)#<class '__main__.Student'>