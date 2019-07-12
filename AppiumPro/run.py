import unittest
from utils.HTMLTestRunner import HTMLTestRunner

testcases = unittest.defaultTestLoader.discover("cases", "test_*.py")

testsuits = unittest.TestSuite()
testsuits.addTests(testcases)

title = "知乎的测试报告!"
descr = "知乎的收藏回答的测试报告!"
file_path = "reports/zhihu_reports.html"

with open(file_path, "wb") as f:
    runner = HTMLTestRunner(stream=f, title=title, description=descr)
    runner.run(testsuits)