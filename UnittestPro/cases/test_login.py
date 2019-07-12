import time
import unittest
from selenium import webdriver

class TestCaseLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\SNake\\VSCodeProjects\\ljtest201906\\UnittestPro\\driver\\chromedriver.exe")
        self.driver.get("http://118.24.29.59:8080/morning/")

    def tearDown(self):
        self.driver.quit()

    def test_01_login(self):
        # 1. 点击登录按钮
        login_page = self.driver.find_element_by_link_text("登录")
        login_page.click()
        # 2.输入用户名和密码登录
        username = self.driver.find_element_by_id("adminNo")
        password = self.driver.find_element_by_id("password")
        login_btn = self.driver.find_element_by_id("btn_login")

        username.send_keys("test@qq.com")
        password.send_keys("a123456")
        login_btn.click()

        time.sleep(5)

        # 3.unittest的断言: 相等
        user_str = self.driver.find_element_by_id("userName").text
        self.assertEqual(user_str, "test")

    def test_02_login_failed(self):
        self.assertFalse(True)