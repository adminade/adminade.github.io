# def hanshu():
#     return '12'
# def test():
#     pass    #占位
# # python函数返回值可多个
# def hh():
#     return 1,2,3,'asdf'
# print(type(hanshu()))
# print(type(hh()))
# def hh1():
#     return 1,2,3,'asdf',{'a','b'}
# print(type(hh1()))
# def sum(a,b):
#     return a+b
# print(sum(1,2))
# def swap(a,b):
#     a,b=b,a
# swap(1,2)
# 函数值传递,swap失败
# 地址传递   :
# 地址传递的实参数据一般是列表或字典列表 ...
# 不可变数据类型 按值传递!   元组  普通的数据类型
#  可变数据类型按地址传递 !    eg 字典 列表 集合
# list_1=[1,2,3]
# def change(list):
#     list.append(4)
#     list=[1,2,3]   #函数里直接复制 意味着定义的是一个新变量
# print(change(list_1))
# def swap(list_2):
#     list_2[0],list_2[1]=list_2[1],list_2[0]
# list_3=[1,2]
# print(list_3)
# print(swap(list_3))

#  函数的默认参数
# 求x得y次方  默认情况下 x的2次方

# def pow(x=2, y=2):
#     return x**y

# print(pow())
# 函数的不定长参数
# def number(numbers):
#     return sum(numbers)
# print(number((1,2,3,4)))


# 类对象

# class nihao():
#     # screensize=15.6
#     # cup='curui_i9'
#     # memosize='512G'
#     def call(self):  # 方法
#         # self 表示类自身
#         print('call')
#     def __init__(self,a,b):
#         self.memosize=b    #初始化 属性传值
#         self.screensize=a

# x=nihao(10.8,12)  #x是类的实例对象
# print(x.screensize)   #属性
# x.call()              #方法

# __del__ 析构方法 回收机制
# import sys


# class nihao():
#     # screensize=15.6
#     # cup='curui_i9'
#     # memosize='512G'
#     def call(self):  # 方法
#         # self 表示类自身
#         print('call')

#     def __init__(self, a, b):
#         self.memosize = b  # 初始化 属性传值
#         self.screensize = a

#     def __del__(self):
#         print('我被del了')


# x = nihao(10.8, 12)  # x是类的实例对象
# print(x.screensize)  # 属性
# x.call()  # 方法
# del x  # 销毁对象。
# # tmp=x
# # temp=x
# # sys.getrefcount(x)   #引用次数
# print(dir(nihao))
# class nihaoya(object)   #继承 object

# 属性分类
# 实例属性：与实例属性相关；  类属性：和类相关
# class mama:
#     pai=3.14
#     def __init__(self,r):
#         self.r=r       #每个实例不同 r不同 实例属性
#     def  s(self):
#         return self.pai* self.r   #pai为类实例，只和和类相关
# x=mama
# print('x1',x.pai)
# print(mama.pai)
# # mama.r 就拿不到
# mama.pai=3.1415926
# print(mama.pai)
# x=mama(2)
# x.pai=32
# print('mamam',mama.pai)


# 动态添加类属性
# class person:
#     def __init__(self,Name,age):
#         self.name=Name
#         self.age=age
# print(dir(person))
# person.sex='男'       #添加类属性 后面都可以使用
# print(dir(person)) 
# lishi=person('账单',13)
# lishi.age=13
# 实例方法  类方法  静态方法
# 类方法定义时需要加上装饰器
# 1、实例方法
# class person:
#     def __init__(self,Name,age):  实例 self本身
#         self.name=Name
#         self.age=age
#     def printinfo(self):
#         print(dir(person))
#     @classmethod  类本身
#     def test(cls):
#         print('test')
#     @staticmethod  静态
#     def test1():
#         print('test1')

# lishi=person('李四',12) 
# lishi.printinfo()  # 1、实例方法只能被实例方法所调用
# person.test # 其他两个都可以通过类名. 调用
# person.test1
# 在变量、函数、类方法的开头一个下滑线 为模块私有，只有类实例和
# class preson1:
#     def __init__（self):
#         self.name='网'        #public   公用
#         self._sex=1            # protected  保护 在他内部或他的子类的内部，都能正常使用，但外部不能使用
#         self.__age=2            #private 私有 只能内部使用
# zhangshang=person1() 
# print(zhangshang.name)
# print(zhangshang.age)
# print(zhangshang.sex)      
# 封装
# 经常用到下划线属性，目的：外部不能直接访问，  通过方法对属性操作！
class animal:
    def __init__(self,name):
        self.name=name
class cat(animal):   #cat 类 继承animal类，拥有父类的属性和方法，  如果子类中没有init 则父类的初始化函数会被调用。
    def __init__(self,name,age):
        super().__init__(name)  # !!!继承父类的init 方法！
        self.age=age
    def maiomiao(self):
        print("miaomiao")
# class chinacat(cat):   #单继承：只有一个直接父类。 多重继承

xiaohua=cat('下滑',5)
