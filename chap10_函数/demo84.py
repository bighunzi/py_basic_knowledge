"""
作者：Big_hunzi
日期：2021年11月05日   12:21

主题：函数的参数总结
"""

def fun(a,b,c):
    print('a=',a)
    print('b=', b)
    print('c=', c)

#函数的调用
fun(10,20,30)
lst=[11,22,33]

#fun(lst)#TypeError: fun() missing 2 required positional arguments: 'b' and 'c'
fun(*lst)#在函数调用时，将列表中的每个元素都转换为位置实参传入

fun(a=100,c=300,b=200)
dic={'a':111,'b':222,'c':333}
#fun(dic)TypeError: fun() missing 2 required positional arguments: 'b' and 'c'
fun(**dic)#在函数调用时，将字典中的键值对都转换为关键字实参传入

def fun1(a,b,c,d):
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)

fun1(10,20,30,40)#位置实参传递
fun1(a=10,b=20,c=30,d=40)



'''
需求：c,d只能采用关键字实参传递
那就要在ab和cd中间加*
'''

def fun2(a,b,*,c,d):
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)

#fun2(10,20,30,40)#TypeError: fun2() takes 2 positional arguments but 4 were given
fun2(10,20,c=30,d=40)
