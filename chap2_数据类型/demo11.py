"""
作者：Big_hunzi
日期：2021年10月23日   17:39

主题：数据类型转换
"""
name='张三'
age=20
print(type(name),type(age))

#print('我叫'+name+'今年'+age+'岁') #将str与int连接时，报错。解决方案：类型转换
print('我叫'+name+'今年'+str(age)+'岁') #将str与int连接时，报错。解决方案：类型转换


#转字符串
a=10
b=198.2
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))


#转int
f1=98.8
ff=True

print(int(f1),type(int(f1)))#取整了 舍去了小数
print(int(ff),type(int(ff)))#


#转浮点数
a1=10
b1='198.2'
c1=False
print(type(a1),type(b1),type(c1))
print(float(a1),float(b1),float(c1),type(float(a1)),type(float(b1)),type(float(c1)))

