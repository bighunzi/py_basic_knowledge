"""
作者：Big_hunzi
日期：2021年11月10日   12:34

主题：被调用的模块
"""
def add(a,b):
    return a+b

if __name__ == '__main__':#只有当点击运行calc2时，才会执行运算
    print(add(10,20))