# 把selenium的测试用例放在unittest中来执行
# 埋坑
import time
import unittest
from selenium import webdriver

class TestCaseMorning(unittest.TestCase):

    # 在类里面，如果不同的方法要引用变量，那么必须把这个变量写成成员变量，即：self.xxxx 
    def setUp(self):
         # 1. 打开浏览器
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\SNake\\VSCodeProjects\\ljtest201906\\SeleniumTest\\chromedriver.exe")
        # 2. 打开猫宁商城
        self.driver.get("http://118.24.29.59:8080/morning/")

    def tearDown(self):
        # 退出测试
        self.driver.quit()

    def test_01_login(self):
        # 3. 点击登录按钮
        login_page = self.driver.find_element_by_link_text("登录")
        login_page.click()
        # 4.输入用户名和密码登录
        username = self.driver.find_element_by_id("adminNo")
        password = self.driver.find_element_by_id("password")
        login_btn = self.driver.find_element_by_id("btn_login")

        username.send_keys("test@qq.com")
        password.send_keys("a123456")
        login_btn.click()

        time.sleep(5)
        # 5.断言登录的结果
        assert self.driver.find_element_by_id("userName").text == "test1"

unittest.main()