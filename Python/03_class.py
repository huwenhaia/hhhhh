# 类的使用
# ****************************** 必须要掌握的  ****************************** 

# 定义一个类
class Phone():

    # 成员变量：就不是普通变量了，类的属性
    size = "5.5"
    name = "Phone"
    price = "10888"

    # 成员方法：功能
    def call(self):
        print("手机可以打电话")

    def sms(self):
        print("手机可以发短信")

    def shipin(self):
        print("手机还可以看视频")


# 实例化对象
p = Phone()

# 获取成员变量
print(p.size)
print(p.name)
print(p.price)

# 调用成员方法
p.call()
p.sms()
p.shipin()
print("**************************************************")
print("**************************************************")


# ****************************** 进阶的内容 ****************************** 

# 补充： 
#       1.类方法的传参
#       2.self：类本身自带了一个实例化对象，他能够在类的内部来调用自己的属性和方法
#       3.继承：类和类之间的关系，被继承的那个类叫父类，继承类叫子类，子类就可以拥有父类的属性和方法了


# 定义人这样一个人类
class Person():
    name = "张三"
    age = 18
    sex = "男"
    money = "1E"

    def tolk(self, text="java好难！"):
        print("我能说:{}".format(text)) # .format 相当于是拼接字符串

    def run(self):
        # 1. 去掉用类的成员变量
        print(self.name)

        # 2.去调用类自己本身的成员方法
        self.tolk()
        
p1 = Person()

# 成员方法的传参
# p1.tolk("python好简单！")     # 传参
# p1.tolk()                    # 不传参
# p1.run()

# 类的继承
class Son(Person):
    name = "小张三"

xzs = Son()
print(xzs.name)
# 子类对象调用父类的属性
print(xzs.money)
# 子类对象调用父类的方法
xzs.tolk()


class GrandSon(Son):
    name = "张三的孙子"
# 孙类同样可以调用祖辈的属性和方法
# grand_son = GrandSon()
# grand_son.name
# grand_son.money
# grand_son.tolk()