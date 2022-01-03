"""
作者：Big_hunzi
日期：2021年11月03日   12:12

主题：集合
python的内置数据结构
与列表，字典一样都属于可变类型的序列
集合是没有value的字典
"""

#集合的创建
s={'hello','python',98}
print(s)


s={0,1,2,2,2,3,3,3,4}#不能重复，如同字典中的键一样
print(s)



#set()
s1=set(range(6))
print(s1,type(s1))
s2=set([3,5,3,6,5,7,1])#将列表中的元素转换为集合中的元素（会去掉重复元素）
print(s2,type(s2))
s3=set((1,2,4,4,5,5,65))#65跑到了前面，说明集合中的元素无序
print(s3,type(s3))

s4=set('python')#字符串序列
print(s4,type(s4))

s5=set({1,2,8,6,6,65})#调用函数，集合中元素顺序又变了
print(s5,type(s5))

#定义空集合
s6={} #字典类型
print(s6,type(s6))

s7=set() #空集合
print(s7,type(s7))
