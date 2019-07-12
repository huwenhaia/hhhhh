# 异常处理：增强代码的稳健性,让程序能够正常执行


# a = 1/0

b = [1,2,3]
# for a in b:
#     print(a)

print(b[0])
print(b[1])
print(b[2])

# 首先去尝试执行代码，如果没有报错，那就不执行except
# 如果报错了，就去执行except关键字下面的代码语句
# try:
#     print(b[3])
# except:
#     print("b[3]报错了")
#     print("b[3]报错了")
#     print("b[3]报错了")
#     print("b[3]报错了")


# finally关键字：无论如何都要去执行finally下面的代码
try:
    # print(b[3])
    print(b[2])
except:
    print("b[3]报错了")
finally:
    print("finally")
