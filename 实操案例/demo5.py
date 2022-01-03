"""
作者：Big_hunzi
日期：2021年11月18日   14:41

主题：
"""
lst=[]
for i in range(0,5):
    goods=input('请输入商品编号与名称进行商品的入库，每次只能输入一件商品:\n')
    lst.append(goods)
print(lst)
for item in lst:
    print(item)

cart=[]
while True:
    num=input('请输入要购买的商品编号:')
    if num == 'q':
        break
    for item in lst:
        if item.find(num)!=-1:
            cart.append(item)
            break
print('您购物车里已经选好的商品为：')
'''for m in cart:
    print(m)
应该倒序输出'''

for i in range(len(cart)-1,-1,-1):
    print(cart[i])