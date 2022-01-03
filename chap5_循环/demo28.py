"""
作者：Big_hunzi
日期：2021年10月27日   21:45

主题：rang函数 用于生成一个整数序列。
     返回值是一个迭代器对象。有点：不管range对象表示的整数序列有多长，所有range对象占用的内存空间都是相同的。
     因为仅仅需要存储start,stop,step,只有当用到range对象时，才会去计算序列中的相关元素。
range()的三种创建方式
"""

#第一种，，只有一个参数  range(stop)
r=range(10)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]，默认从零开始，默认相差1为步长
print(r) #range(0, 10)  
print(list(r)) #用于查看range对象中的整数序列  -->list是列表的意思

#两个参数  range(start,stop)
r=range(1,10)
print(list(r))

#三个参数 range(start,stop,step)
r=range(1,10,2)
print(list(r))



#判断指定整数在序列中是否存在。 in,not in
print(9 in r)
print(10 in r)
