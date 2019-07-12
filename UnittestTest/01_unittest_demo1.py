# 1. 导入unittest
import unittest

# 2. 新建一个类，组织测试用例，这个类必须去继承unittest.TestCase
class TestCaseDemo1(unittest.TestCase):

    # 3. 测试方法：测试用例
    # unittest默认去查找test开头的成员方法，, test_
    # unittest三段式命令
    def test_03_aa(self):
        # 登录
        print("aaaa")

    def test_01_bb(self):
        # 搜索商品
        print("bbbb")

    def test_02_cc(self):
        # 下单
        print("cccc")

# 普通类的写法，自动化就不这样写
# demo1 = TestCaseDemo1()
# demo1.test_aa()

# 主要用在调试unittest脚本的时候会使用到
# unittest.main()