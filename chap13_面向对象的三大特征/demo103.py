"""
作者：Big_hunzi
日期：2021年11月09日   19:14

主题：
特殊方法：
_len_():通过重写_len_()方法，让内置函数len()的参数可以是自定义类型
_add_():通过重写_add_()方法,可使用自定义对象具有“+”功能

"""

a=20
b=100
c=a+b
print(c)

d=a.__add__(b)
print(d)

class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name
    def __len__(self):
        return len(self.name)

stu1=Student('张三')
stu2=Student('李四')

print(stu1+stu2)#实现了两个对象的加法运算，因为在Student类中编写了_add_()特殊方法
print(stu1.__add__(stu2))


print('-------------------------')
lst=[11,22,33,44]
print(len(lst))#len是内置函数，可以计算列表长度
print(lst.__len__())


print(len(stu1))#不定义_len_的话：ypeError: object of type 'Student' has no len()

