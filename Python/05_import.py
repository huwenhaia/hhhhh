# 包和模块
# 包：python的文件夹，这个文件夹包含了一个__init__.py的文件
# 包：用来放py文件

# 模块：py文件

# =====================================================

# 导入

# ********************************* 简单 必须要掌握的

# 1. 为什么要导入：因为要使用另外的py文件的内容

# 2. 可以入导入些什么内容呢？

# 变量 a shanchu
# 方法：test
# 类：Person

# 3. 同级如何导入
import pymysql # 第三库、原生自带的库

# 这种通常用在同级的目录下
from test_import import a
from test_import import test
from test_import import Person

print(a)
test()
p = Person()
print(p.username)

# ********************************* 进阶，在不同级

from bao.test import a
from bao.test import test1
from bao.test import Person