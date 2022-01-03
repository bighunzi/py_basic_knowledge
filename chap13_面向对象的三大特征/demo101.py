"""
作者：Big_hunzi
日期：2021年11月08日   19:34

主题：多态
简单地说，多态就是“具有多种形态”，它指的是：即便不知道一个变量所引用的对象到底是什么类型，仍然可以通过这个变量调用方法，
在运行过程中根据变量所引用的类型，动态决定调用哪个对象中的方法


静态语言实现多态的三个必要条件：继承、方法重写、父类引用指向子类对象
动态语言的多态崇尚“鸭子类型”，当看到一只鸟走起来像鸭子、游泳起来像鸭子、收起来也像鸭子，那么这只鸟就可以被称为鸭子
在鸭子类型中，不需要关心对象是什么类型，到底是不是鸭子，只关心对象的行为。
"""
class Animal:
    def eat(self):
        print('动物会吃')

class Dog(Animal):
    def eat(self):
        print('狗吃肉')

class Cat(Animal):
    def eat(self):
        print('猫吃鱼')

class Person(Animal):
    def eat(self):
        super().eat()


#定义一个函数
def fun(obj):
    obj.eat()

#开始调用函数
fun(Cat())#加括号才是实例对象，不加括号只是类对象
fun(Dog())
fun(Animal())

print('----------------------------')
fun(Person())#自己没有整个函数，就调用父类的