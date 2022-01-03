"""
作者：Big_hunzi
日期：2021年11月17日   12:13

主题：
"""
filename='1.txt'
fp=open(filename,'w')
print('奋斗成就更好的你',file=fp)
fp.close()

with open('2.txt','w') as wfile:
    wfile.write('奋斗成就更好的你')


