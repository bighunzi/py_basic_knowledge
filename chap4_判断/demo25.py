"""
作者：Big_hunzi
日期：2021年10月27日   11:47

主题：嵌套if

会员： >=200 八折
      >=100 9折
      <100 八折
非会员：>=200 9.5折
      <200 不打折
"""
answer=input('您是会员么？y/n')
money=float(input('请输入您的购物金额：'))
if answer=='y':
    print('会员')
    if money>=200:
        print('付款金额为：',money*0.8)
    elif money>=100:
        print('付款金额为：',money*0.9)
    else:
        print('付款金额为：',money)

else:
    print('非会员')
    if money>=200:
        print('付款金额为：',money*0.95)
    else:print('付款金额为：',money)
