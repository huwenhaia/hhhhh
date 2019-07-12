
# ********************* 课程内容 *******************
# 掌握查询、增加、修改、删除方法的的调用
# 进阶: 如它的实现思路
# *************************************************

# 导入pymysql
# 要使用pymysql：首先必须要在命令行里面安装pymysql，pip3 install pymysql -i https://pypi.tuna.tsinghua.edu.cn/simple
import pymysql

# ******************************************** 查询

# 调用这个query方法的时候，传入一句sql，这个query方法就返回数据库的结果给我们
# sql是指参数，也就是我们想要执行的sql语句
def query(sql):
    """
       数据库的查询功能，传入一个sql参数 
    """
    # 1. 定义第一个字典，存放数据库的信息
    dbinfo = {
        "host": "118.24.29.59",             # 数据库的地址
        "user": "vn",                       # 用户名
        "password": "1qaz!QAZ123",          # 密码
        "db": "lux"                         # 数据库的名字
    }
    # 2. 连接数据库：去链接并且打开数据库
    db = pymysql.connect(**dbinfo)
    # 3. 获取游标:去获取查询窗口
    cursor = db.cursor()
    # 4. 去执行sql
    cursor.execute(sql)
    # 5.获取返回值
    res = cursor.fetchall()
    # 6. 返回结果
    return res

# 去调用sql,调用方法一定要放在方法的外面
# a = "select * from tbl_admin;"
# res = query(a)
# print(res)


# ****************************************** 增加、修改、删除
def commit(sql):
    """
        数据库的增加/修改/删除
    """
    dbinfo = {
        "host": "118.24.29.59",             # 数据库的地址
        "user": "vn",                       # 用户名
        "password": "1qaz!QAZ123",          # 密码
        "db": "lux"                         # 数据库的名字
    }
    db = pymysql.connect(**dbinfo)
    cursor = db.cursor()

    # 执行成功：返回True；执行失败：返回False
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except:
        return False


# 执行insert语句: 外双内单；外单内双
# charu = 'INSERT INTO tbl_admin VALUES(NULL, "admin3", "admin3", 1, '',  1, "2018-03-29 15:41:03", NULL)'
# charu = "INSERT INTO tbl_admin VALUES(NULL, 'admin3', 'admin3', 1, '',  1, '2018-03-29 15:41:03', NULL)"
# commit(charu)

# 执行update语句
# xiugai = "update tbl_admin SET `password`='hello';"
# commit(xiugai)

# 执行delete语句
shanchu = "delete FROM tbl_admin where id=3;"
commit(shanchu)