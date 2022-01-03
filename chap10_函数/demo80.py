"""
作者：Big_hunzi
日期：2021年11月04日   20:08

主题：函数参数传递的内存分析
"""
def fun(arg1,arg2):
    print('arg1',arg1,id(arg1))
    print('arg2', arg2, id(arg2))
    arg1=100
    arg2.append(10)
    print('arg1',arg1,id(arg1))
    print('arg2', arg2, id(arg2))

n1=11
n2=[22,33,44]
print('n1',n1,id(n1))
print('n2',n2,id(n2))
fun(n1,n2)#由于它不执行任何结果，所以上面的函数不用return

print('n1',n1,id(n1))
print('n2',n2,id(n2))


'''
在函数调用过程中，进行参数的传递
如果是不可变对象，在函数体的修改不会影响实参的值：n1：11。arg1的修改为100，不会影响n1的值
如果是可变对象，在函数体内的修改会影响到实参的值：n2.arg2的修改。append(10),会影响到n2的值
'''