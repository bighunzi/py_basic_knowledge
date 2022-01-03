"""
作者：Big_hunzi
日期：2021年11月07日   15:54

主题：对象的创建
对象的创建又称为类的实例化
#实例名=类名()
有了实例，就可以调用类中的内容

有一个图 可以看看

"""
class Student:#Student就是类名，由一个或多个类名组成，每个单词的首字母大写，其余小写。(这是规范，不这么写也不报错)
    native_place='吉林'#直接写在类里的变量，称为类属性

    def __init__(self,name,age):#初始化方法
        self.name=name#self.name称为实例属性，进行了一个赋值操作，将局部变量的name的值赋给了实例属性
        self.age=age

    def eat(self):#实例方法(类之内成为方法，类之外成为函数)
        print('学生在吃饭...')

    @staticmethod
    def method():#静态方法
        print('我是用了staticmethod进行修饰，所以我是静态方法')

    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')

#创建Student类的对象
stu1=Student('张三',20)
print(id(stu1))#2784694609472  十进制
print(type(stu1))
print(stu1)#0x000002885CBBA640 十六进制

stu1.eat()
print(stu1.name)
print(stu1.age)


Student.eat(stu1)#与stu1.eat()作用相同，都是调用Student中的eat方法
                 #类名.方法名(类的对象)-->实际就是方法定义处的self