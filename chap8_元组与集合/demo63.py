"""
作者：Big_hunzi
日期：2021年11月03日   12:28

主题：集合的相关操作
"""
s={10,20,30,405,60}
print(10 in s)
print(50 not in s)

#新增操作
s.add(80)
print(s)

s.update({200,400,300})
print(s)

s.update([100,99,8])#放列表
print(s)
s.update((98,65,85))#放元组
print(s)


#删除操作
s.remove(100)
print(s)

s.discard(500)#删除并不存在的元素，并不会报错
print(s)
s.discard(300)
print(s)


s.pop()#一次只删除一个任意元素
print(s)

s.pop()#一次只删除一个任意元素
print(s)

s.clear()
print(s)
