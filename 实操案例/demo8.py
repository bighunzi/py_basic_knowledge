"""
作者：Big_hunzi
日期：2021年11月19日   12:34

主题：
"""
def is_triangle(a,b,c):
    if a<0 or b<0 or c<0:
        raise Exception('三条边不能是负数')

    if a+b>c and a+c>b and b+c>a:
        print(f'三角形边长为a={a},b={b},c={c}')
    else:
        raise Exception(f'a={a},b={b},c={c},不能构成三角形')

