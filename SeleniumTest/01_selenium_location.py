# ********************************* 非常重要：必须要掌握的元素定位方法和对应的方式

import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()

driver.get("http://118.24.29.59:8080/morning/")

# 定位方式：八种定位元素的方式

# 1. id：能用id就用id
# e = driver.find_element_by_id("searchInput")    # 去网页中查找到id值为searchInput的元素
# e.send_keys("iPhone")                           # 去这个输入框中输入一个字符串：iPhone

# 2. xpath：不能用id就用xpath
# e1 = driver.find_element_by_xpath('//*[@id="zySearch"]/button')
# e1.click()                                      # 去点击一下这个按钮

# 3. link text：用得比较多的
# e2 = driver.find_element_by_link_text("登录")
# e2.click()                                          # 去点击登录

# 4. partial link text
# e3 = driver.find_element_by_partial_link_text("登")
# e3.click()

# 5. css selector
e4 = driver.find_element_by_css_selector("#mian-nav-right-login > a:nth-child(1)")
e4.click()

# 6. name
e5 = driver.find_element_by_name("user.loginName")
e5.send_keys("13000000001")

# 等待3s，必须要import time才能使用sleep
time.sleep(3)

# 7. class
e6 = driver.find_element_by_class_name("current")
e6.click()

# 8.tag name：不重要
e7 = driver.find_element_by_tag_name("a")
print(e7.text)
