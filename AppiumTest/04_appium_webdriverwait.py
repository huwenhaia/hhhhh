# **************************** 进阶：动态查找元素 **************************** 
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


desired_caps = {}
desired_caps['platformName'] = 'Android'                    # 打开什么平台的app，固定的 > 启动安卓平台
desired_caps['platformVersion'] = '5.1.1'                   # 安卓系统的版本号：adb shell getprop ro.build.version.release
desired_caps['deviceName'] = 'vivo x6plus d'                # 手机/模拟器的型号：adb shell getprop ro.product.model
desired_caps['appPackage'] = 'io.appium.android.apis'       # app的名字：adb shell dumpsys activity | findstr "mFocusedActivity"
desired_caps['appActivity'] = '.ApiDemos'                   # app的启动页名字：adb shell dumpsys activity | findstr "mFocusedActivity"
desired_caps['unicodeKeyboard'] = True                      # 为了支持中文
desired_caps['resetKeyboard'] = True                        # 设置成appium自带的键盘

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)



"""
    id: "id"
    xpath: "xpath"
    accessibility_id: "accessibility id"
    android_uiautomator: "-android uiautomator"
"""
# locator = ("xpath", '//android.widget.TextView[@content-desc="App"]')
locator = ("id", 'android:id/text1')
app = WebDriverWait(driver, 30).until(lambda s: s.find_element(*locator))
app.click()