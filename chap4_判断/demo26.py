"""
作者：Big_hunzi
日期：2021年10月27日   11:59

主题：从键盘录入两个整数，比较其大小.
"""
num_a=int(input('请输入第一个整数：'))
num_b=int(input('请输入第二个整数：'))

#比较大小
'''if num_a>=num_b:
    print(num_a,'大于等于',num_b)
else:
    print(num_a,'小于',num_b)
'''

#简写  使用条件表达式
print(num_a,'大于等于',num_b if num_a>=num_b else num_a,'小于',num_b) #没有括号不对

print((num_a,'大于等于',num_b) if num_a>=num_b else (num_a,'小于',num_b))

print(str(num_a)+'大于等于'+str(num_b) if num_a>=num_b  else  str(num_a)+'小于'+str(num_b))#+只能连接同种数据


