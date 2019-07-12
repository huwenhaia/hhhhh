import time
import unittest
from appium import webdriver


class TestCaseZhihu(unittest.TestCase):
    
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'                    
        desired_caps['platformVersion'] = '5.1.1'                   
        desired_caps['deviceName'] = 'vivo x6plus d'                
        desired_caps['appPackage'] = 'com.zhihu.android'            
        desired_caps['appActivity'] = '.app.ui.activity.MainActivity' 
        desired_caps['unicodeKeyboard'] = True                      
        desired_caps['resetKeyboard'] = True                        

        # 去打开app，并且返回当前app的操作对象
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()
        print("测试结束")

    def test_01_collect(self):
        password_login = self.driver.find_element_by_id("com.zhihu.android:id/go_to_btn")
        password_login.click()
        
        # 登录操作
        username = self.driver.find_element_by_id("com.zhihu.android:id/email_input_view")
        username.send_keys("13687125001")

        password = self.driver.find_element_by_id("com.zhihu.android:id/password")
        password.send_keys("12345678q")

        login_btn = self.driver.find_element_by_id("com.zhihu.android:id/btn_progress")
        login_btn.click()

        time.sleep(10)

        # 断言登录是否成功
        my = self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")') 
        self.assertIsNotNone(my.text)




    