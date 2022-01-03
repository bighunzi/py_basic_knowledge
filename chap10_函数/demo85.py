"""
作者：Big_hunzi
日期：2021年11月05日   21:40

主题：变量的作用域
程序代码能访问该变量的区域

根据变量的有效范围可分为：
局部变量：在函数内定义并使用的变量，只在函数内部有效
        局部变量使用global声明，这个变量就会变成全局变量
全局变量：函数体外定义的变量，可作用与函数内外。

"""

def fun(a,b):#a,b是形参，作用范围也是函数内部，相当于局部变量
    c=a+b#c就是局部变量
    print(c)


name='big_hunzi'#全局变量
def fun1():
    print(name)

fun1()


def fun2():
    global age
    age=20
    print(age)

fun2()
print(age)