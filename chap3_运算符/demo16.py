"""
作者：Big_hunzi
日期：2021年10月25日   16:36

主题：赋值运算符
"""

a=b=c=20
print(a,id(a))
print(b,id(b))
print(c,id(c))#内存地址相同   a,b,c中存储的内存地址相同，同时指向一个数。



#参数赋值
a+=30# a=a+30
print(a)

a/=3
print(a)
a//=2
print(a)
a%=3
print(a)



#系列解包赋值
a,b,c=20,30,40
print('a=',a,'b=',b,'c=',c)

#交换两个变量的值
print('交换之前：',a,b)
a,b=b,a
print('交换之后：',a,b)