"""
作者：Big_hunzi
日期：2021年11月09日   21:50

主题：类的赋值与拷贝
（类）变量的赋值操作：只是形成两个变量，实际上还是指向一个对象
浅拷贝：Python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝。
       因此，源对象与拷贝对象会引用同一个子对象
深拷贝：使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象。
       源对象和拷贝对象所有的子对象也不相同
"""

class Cpu:
    pass
class Disk:
    pass

class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

cpu1=Cpu()
cpu2=cpu1#其实只有一个实例对象。只不过cpu1 cpu2都指向这个实例对象
print(cpu1)
print(cpu2)

print('--------------------------------')
#类的浅拷贝
disk1=Disk()
computer1=Computer(cpu1,disk1)#要理解 赋值 与等号右面 加起来一共两个操作。这样才会理解 指针，实例对象，类对象

#开始浅拷贝
import copy
computer2=copy.copy(computer1)
print(computer1,computer1.cpu,computer1.disk)
print(computer2,computer2.cpu,computer2.disk)


print('--------------------------------------------')
#深拷贝
computer3=copy.deepcopy(computer1)
print(computer1,computer1.cpu,computer1.disk)
print(computer3,computer3.cpu,computer3.disk)