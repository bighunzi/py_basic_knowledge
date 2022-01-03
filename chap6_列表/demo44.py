"""
作者：Big_hunzi
日期：2021年10月29日   17:51

主题：获取列表中的多个元素(切片)
列表名[start:stop:step] step 默认为1
"""
lst1=[10,20,30,40,50,60,70,80]
print('原列表',id(lst1))
lst2=lst1[1:6:1]
print(lst2,id(lst2))



#step为整数
print(lst1[:6:1])#默认从0开始
print(lst1[1::1])#默认到最后一位

#step为负数  倒序输出
print(lst1[::-1])#
print(lst1[7::-1])#同左闭右开
print(lst1[:2:-1])