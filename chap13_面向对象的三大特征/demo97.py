"""
作者：Big_hunzi
日期：2021年11月07日   18:06

主题：封装

面向对象的三大特征：封装、继承、多态
封装：提高程序的安全性
     将数据（属性）和行为（方法）包装到类对象中包装到类对象中。在方法内部对属性进行操作，在类对象的外部调用方法。这样，无需关心方法内部的具体实现
     细节，从而隔离了复杂度。
     在Python中没有专门的修饰符用于属性的私有，如果该属性不希望在类对象外部被访问，前边使用两个“_”

继承：提高代码的复用性
多态：提高程序的可扩展性和可维护性
"""
#将数据（属性）和行为（方法）包装到类对象中包装到类对象中。
class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('汽车已启动...')

car=Car('宝马X5')
car.start()
print(car.brand)


#在Python中没有专门的修饰符用于属性的私有，如果该属性不希望在类对象外部被访问，前边使用两个“_”
class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age#不希望被外部访问
    def show(self):
        print(self.name,self.__age)

stu=Student('张三',20)
stu.show()

#在类的外部使用age
#print(stu.age)#AttributeError: 'Student' object has no attribute 'age'

print(dir(stu))
print(stu._Student__age)#在类的外部可以通过 _Student__age 进行访问（君子协议）
