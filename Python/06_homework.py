"""
 写一个方法add_user，
 这个方法支持传入一个参数，
 这个参数的格式是字典{"username":"test", "password": "123456"}；
 这个方法必须返回一个list，list的内容是["test", "123456"]
"""

def add_user1(user):
    return list(user.values())

u = {
    "username": "ljtest",
    "password": "123456",
    "sex": "男"
}

b = add_user1(u)
print(b)

# *********************** 理解 ***********************
def add_user(user):
    # 1. 定义一个list变量，用来存储user的所有value
    values = []

    # 2. 去解析这个字段user，并且把value值依次存放在list中
    for k in user:
        v = user[k]             # 字典的每一个value
        values.append(v)        # 把每一个value值添加到list

    # 3. 返回这个list
    return values

u = {
    "username": "ljtest",
    "password": "123456",
    "sex": "男"
}

a = add_user(u)
print(a)
