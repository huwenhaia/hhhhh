import time
import unittest
from selenium import webdriver

class TestCaseIndex(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\SNake\\VSCodeProjects\\ljtest201906\\UnittestPro\\driver\\chromedriver.exe")
        self.driver.get("http://118.24.29.59:8080/morning/")

    def tearDown(self):
        self.driver.quit()

    def test_01_search_goods(self):
        search = self.driver.find_element_by_id("searchInput")
        search.send_keys("unittest大法好!")
    