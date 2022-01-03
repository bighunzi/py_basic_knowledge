"""
作者：Big_hunzi
日期：2021年11月08日   19:23

主题：object类
object类是所有类的父类，因此所有类都有object类的属性和方法。
内置函数dir()可以查看指定对象所有属性
Object有一个_str_()方法，用于返回一个对于“对象的描述”，对应于内置函数str()经常用于print()方法，帮我们查看对象的信息，所以我们经常会对_str_()
进行重写
"""
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '我的名字是{0},今年{1}岁了'.format(self.name,self.age)#格式化字符串

stu=Student('张三',20)
print(dir(stu))

print(stu)#<__main__.Student object at 0x000001062E71E250>
          #会默认调用_str_()方法。
          #所以重写后输出就变了