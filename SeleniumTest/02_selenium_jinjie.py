# ***************************** 进阶 ***************************** 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# 鼠标事件
# -双击
# -右键
# -移动到元素上面

# 键盘事件
# -刷新
# -删除

# driver作用域
# - iframe
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()
driver.get("https://passport2.eastmoney.com/pub/login")

# 1. 切换到子网页的作用域
iframe = ("id", "frame_login")
e = WebDriverWait(driver, 3).until(lambda s: s.find_element(*iframe))      # 首先找到iframe
driver.switch_to_frame(e)                                                  # 切换到iframe

username = ("id", "txt_account")
e = WebDriverWait(driver, 3).until(lambda s: s.find_element(*username))
e.send_keys("1300000001")

# 如果需要找父元素了，就要切换到默认的作用域，大网页
driver.switch_to_default_content()

# 2. 找大网页的元素
addd = ("link text", "东方财富网免费版")
e = WebDriverWait(driver, 3).until(lambda s: s.find_element(*addd))
e.click()

# - 新窗口


# 二次封装
# pyselenium: https://github.com/testjie/PySelenium

