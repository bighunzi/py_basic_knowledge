"""
作者：Big_hunzi
日期：2021年11月07日   16:32

主题：动态绑定属性和方法
Python是动态语言，在创建对象之后，可以动态的绑定属性和方法
"""

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name+'在吃饭')

stu1=Student('张三',20)
stu2=Student('李四',30)
print(id(stu1))
print(id(stu2))
#一个Student类可以创建N多个Student类的实例对象，每个实例对象的属性值不同。
print('----------------为stu2动态绑定性别属性------------------')
stu2.gender='女'
print(stu1.name,stu1.age)
print(stu2.name,stu2.age,stu2.gender)

print('-----------------动态绑定方法-------------------------')
stu1.eat()

def show():
    print('定义在类之外的，称函数')

stu1.show=show
stu1.show()