# 方法（函数）：共用的代码块，它能够提供固定的作用

# *********************************************** 不要参数的
# 参数可以不要；return也是可以不要的
def add2():
    return 1 + 1

# print(add2())

def hello():
    print("hello python!")

# 调用方法
hello()

# *********************************************** 必须要参数的

# python:命令方法英文开头，可以是这样的方式：test_add （test_01_xxx）
def add(a1, b1):
    return a1 + b1

# 这种情况就会报错
# print(add())

a = 1
b = 2

# 调用方法之前
# c = a + b
# d = c + a

# 调用方法之后
c = add(a, b)
d = add(c, a)

print(c)
print(d)


# *********************************************** 有默认值参数的-进阶内容

# a和b是方法的参数，参数是可以有默认值的,
# 允许调用方法的时候不传递参数
# 还可以只传一部分参数
def add1(a=10, b=100):
    return a + b

# 传参
# sum = add1(a=1000, b=1000)
# print(sum)

# 传递一部分参数,可以不分顺序
add1()
add1(100, 10000)
sum1 = add1(a=100)
sum2 = add1(b=100)
sum2 = add1(b=100, a=10000)
print(sum1)
print(sum2)
