"""
作者：Big_hunzi
日期：2021年11月03日   12:37

主题：集合间的关系
"""
s1={10,20,30,40}
s2={30,40,20,10}
print(s1==s2) #集合中元素无序


#一个集合是否是另外一个集合的子集
s3={10,40}
s4={10,50}
print(s3.issubset(s1))
print(s4.issubset(s1))

#一个集合是否是另外一个的超集
print(s1.issuperset(s3))
print(s1.issuperset(s4))

#两个集合是否有交集
print(s1.isdisjoint(s4)) #False  s1,s4有交集
s5={100,200,300}
print(s1.isdisjoint(s5))#True  s1,s5没有交集