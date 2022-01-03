"""
作者：Big_hunzi
日期：2021年10月26日   23:09

主题：多分枝结构  多选一执行

从键盘录入一个整数成绩
90-100 A
80-89  B
70-79  C
60-69  D
0-59   E
小于0或大于100为非法数据
"""
score=int(input('请输入一个成绩：'))
if 90<=score<=100:
    print('A级')
elif score>=80 and score<=89:
    print('B级')
elif score>=70 and score<=79:
    print('C级')
elif score>=60 and score<=69:
    print('D级')
elif score>=0 and score<=59:#注意冒号
    print('E级')
else:
    print('对不起，成绩有误')
