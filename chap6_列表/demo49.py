"""
作者：Big_hunzi
日期：2021年10月31日   19:17

主题：列表元素的排序操作
"""
lst=[20,5,16,8,50]
print('原列表：',lst,id(lst))
#调用列表中的sort方法，升序排序
lst.sort()
print('排序后列表',lst,id(lst))


#通过关键字参数，降序排列
lst.sort(reverse=True)
print('排序后列表',lst,id(lst))

lst.sort(reverse=False)
print('排序后列表',lst,id(lst))




#sorted排序，将产生一个新的列表对象
lst=[20,5,16,8,50]
print('原列表：',lst)
new_lst1=new_lst=sorted(lst)
print('排序后列表',new_lst,id(lst),'\n',new_lst1,id(new_lst1))

#同样 关键字参数
desc_lst=sorted(lst,reverse=True)
print('排序后列表',desc_lst,id(desc_lst))
