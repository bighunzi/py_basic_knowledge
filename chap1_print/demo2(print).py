"""
作者：Big_hunzi
日期：2021年10月23日   15:09

主题：转义字符
"""

#转义字符
print('hello\nworld') #\n换行
print('hello\tworld') #\t占用四个空格的位置
print('helloooo\tworld')
print('hello\rworld') #\r将光标回退本行开头位置（覆盖）
print('hello\bworld')#\b退一个格，（将o退没了）


print('http:\www.baidu.com')
print('http:\\www.baidu.com')#\\两个转出一个
print('http:\\\\www.baidu.com')
print('老师说：\'大家好\'')# ''不再是边界，而是应该输出的内容

#原字符，不希望字符串中的转义字符起作用，就是用原字符，就是在字符串之前加上r，或R
print(r'hello\nworld')
#注意事项，最后一个字符不能是'\'
#print(r'hello\nworld')
print(r'hello\nworld\\')