"""
作者：Big_hunzi
日期：2021年11月19日   11:28

主题：
"""
try:
    score=int(input('请输入分数：'))
    if 0<=score<=100:
        print('分数为：',score)
    else:
        raise Exception('分数不正确')#抛出异常
except Exception as e:
    print(e)