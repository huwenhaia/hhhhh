import unittest

class TestCaseLift(unittest.TestCase):
    # 类方法：
    @classmethod
    def setUpClass(cls):
        # 初始化的操作放在这个方法下面
        # 比如说selenium的 webdriver.Chrome("")
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        # driver.quit()
        print("tearDownClass")

    def setUp(self):
        # selenium的 webdriver.Chrome("")
        print("setUp")

    def tearDown(self):
        # driver.quit()
        print("tearDown")

    def test_01(self):
        print("test_01")   

    def test_02(self):
        print("test_02")   

    def test_03(self):
        print("test_03")        


unittest.main()