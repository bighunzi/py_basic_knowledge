"""
作者：Big_hunzi
日期：2021年11月18日   14:33

主题：
"""
year=[88,89,92,99,00,98]
print('原列表',year)
for index,value in enumerate(year):#enumerate 是给索引值
    print(index,value)
    if str(value)!='0':
        year[index]=int('19'+str(value))
    else:
        year[index]=int('200'+str(value))

print('修改之后的列表',year)