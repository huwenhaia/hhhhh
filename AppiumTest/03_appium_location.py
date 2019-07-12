# ************************ 基础：掌握 *********************************

from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'                    # 打开什么平台的app，固定的 > 启动安卓平台
desired_caps['platformVersion'] = '5.1.1'                   # 安卓系统的版本号：adb shell getprop ro.build.version.release
desired_caps['deviceName'] = 'vivo x6plus d'                # 手机/模拟器的型号：adb shell getprop ro.product.model
desired_caps['appPackage'] = 'io.appium.android.apis'       # app的名字：adb shell dumpsys activity | findstr "mFocusedActivity"
desired_caps['appActivity'] = '.ApiDemos'                   # app的启动页名字：adb shell dumpsys activity | findstr "mFocusedActivity"
desired_caps['unicodeKeyboard'] = True                      # 为了支持中文
desired_caps['resetKeyboard'] = True                        # 设置成appium自带的键盘

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


# 1. by_id > resource id : 在安卓软件中，id就不是唯一的值
# accessibility = driver.find_element_by_id('android:id/text1')
# accessibility.click()

# 2. by_xpath > xpath
app = driver.find_element_by_xpath('//android.widget.TextView[@content-desc="App"]')
app.click()

# 获取文本值
print(app.text)

# 3. accessibility id
app_search = driver.find_element_by_accessibility_id('Search')
app_search.click()

# 4. 文本值 >   new UiSelector().text("这里写文本值"): 文本值是非常好用的
app_search_invoke = driver.find_element_by_android_uiautomator('new UiSelector().text("Invoke Search")')
app_search_invoke.click()


# 输入操作
prefill_query = driver.find_element_by_id('io.appium.android.apis:id/txt_query_prefill')
# prefill_query.send_keys("hello 珊珊！") # 支持中文 > 粘贴复制的方法


# *************************** 进阶 *********************
driver.set_value(prefill_query, "hello shanshan") # 只支持英文

# 返回
driver.back()
# home键
driver.press_keycode(3)

# 滑动
import time
time.sleep(3)

for i in range(10):
    driver.swipe(10, 800, 890, 800)
    time.sleep(1)

driver.quit()