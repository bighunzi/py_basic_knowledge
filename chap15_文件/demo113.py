"""
作者：Big_hunzi
日期：2021年11月13日   16:12

主题：常用的文件打开类型

文件的类型：
按文件中数据的组织形式，文件分为一下两大类
文本文件：存储的是普通“字符”文本，默认为unicode字符集，可以使用记事本程序打开。
二进制文件：把数据内容用“字节”，无法用记事本打开，必须使用专业的软件打开

r:以只读模式打开文件，文件的指针将会放在文件的开头
w:以只写模式打开文件，如果文件不存在则创建，如果文件存在，则覆盖原有内容，文件指针在文件开头。
a:以追加模式打开文件，如果文件不存在则创建 ，文件指针在文件开头；如果文件存在，则在文件末尾追加内容，文件指针在源文件末尾。
b:以二进制方式打开文件，不能单独使用，需要与其他模式一起使用，rb或者wb
+:以读写方式打开文件，不能单独使用，需要与其他模式一起使用，a+
"""


file=open('b.txt','w')#打开或创建文件
file.write('Python')
file.close()

file=open('b.txt','a')
file.write('Python')
file.close()

src_file=open('zuorongda.png','rb')
target_file=open('copyzuorongda.png','wb')

target_file.write(src_file.read())

target_file.close()
src_file.close()

'''使用with语句再写一次复制图片'''
with open('zuorongda.png','rb') as src_file:
    with open('copy2zuorongda.png','wb') as target_file:
        target_file.write(src_file.read())