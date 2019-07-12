# 作用是：为我们的开发框架提供一个运行的入口
# 我们只需要运行run.py，然后就能自动化加载所有测试用例，并执行完成后，自动动生成测试报告


"""
    1. cases：用来放测试用例代码的
    2. driver：用来放驱动文件的
    3. report：用来放测试报告的
    4. utils：用来放工具代码的
    5. run.py：为自动化测试框架提供一个运行的入口
"""

# 1. 导入unittest
import unittest
from utils.HTMLTestRunner import HTMLTestRunner

# 2. 让unittest自动化去查找cases文件夹下面的所有测试用例
testcases = unittest.defaultTestLoader.discover("cases", "test_*.py")

# 3. 把所有测试用例加载到测试集里面
testsuits = unittest.TestSuite()
testsuits.addTests(testcases)

# 4. 去运行测试集并且生成测试报告
title = "测试报告"                              # 测试报告的网页title
descr = "猫宁商城测试报告!"
file_path = "report/morning_reports.html"       # 测试报告的描述

with open(file_path, "wb") as f:                # 新建一个html文件，并且把文件对象赋值给f变量
    runner = HTMLTestRunner(stream=f, title=title, description=descr)       # 把测试结果放到这个html文件里面，就是去填写测试报告的内容
    runner.run(testsuits)                       # 去运行所有的测试集