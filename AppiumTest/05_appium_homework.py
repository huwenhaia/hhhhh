# 作业：使用自己注册账号登录知乎，一定要登录成功，并且去断言登录成功之后的元素是否存在

from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'                    # 打开什么平台的app，固定的 > 启动安卓平台
desired_caps['platformVersion'] = '5.1.1'                   # 安卓系统的版本号：adb shell getprop ro.build.version.release
desired_caps['deviceName'] = 'vivo x6plus d'                # 手机/模拟器的型号：adb shell getprop ro.product.model
desired_caps['appPackage'] = 'com.zhihu.android'            # app的名字：adb shell dumpsys activity | findstr "mFocusedActivity"
desired_caps['appActivity'] = '.app.ui.activity.MainActivity'                   # app的启动页名字：adb shell dumpsys activity | findstr "mFocusedActivity"
desired_caps['unicodeKeyboard'] = True                      # 为了支持中文
desired_caps['resetKeyboard'] = True                        # 设置成appium自带的键盘

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 去点击密码登录
driver.find_element_by_id('com.zhihu.android:id/go_to_btn').click()



# 退出测试
driver.quit()