from selenium import webdriver


# # 打开浏览器并且进入猫宁首页
# driver = webdriver.Chrome(executable_path="C:\\Users\\SNake\\VSCodeProjects\\ljtest201906\\SeleniumTest\\chromedriver.exe")
# driver.get("http://118.24.29.59:8080/morning/")

# # 去登录页面
# login_page = driver.find_element_by_xpath('//*[@id="mian-nav-right-login"]/a[1]')
# login_page.click()

# # 输入账户名
# username = driver.find_element_by_xpath('//*[@id="adminNo"]')
# username.send_keys("2941635995@qq.com")

# # 输入密码
# password = driver.find_element_by_xpath('//*[@id="password"]')
# password.send_keys("12345678")

# # 点击登录按钮
# login_btn = driver.find_element_by_xpath('//*[@id="btn_login"]')
# login_btn.click()

# # 断言登录失败的提示语是否存在
# login_failed_msg = driver.find_element_by_xpath('//*[@id="verifyCheck"]/div/div[1]/label')
# assert login_failed_msg.text == "你输入的密码和账户名不匹配，请确认后重新输入。"

# print("测试用例通过了！")

# ************************************************* 

import time

# 打开浏览器并且进入猫宁首页
driver = webdriver.Chrome(executable_path="C:\\Users\\SNake\\VSCodeProjects\\ljtest201906\\SeleniumTest\\chromedriver.exe")
driver.get("http://118.24.29.59:8080/morning/")

# 去登录页面
login_page = driver.find_element_by_xpath('//*[@id="mian-nav-right-login"]/a[1]')
login_page.click()

# 输入账户名
username = driver.find_element_by_xpath('//*[@id="adminNo"]')
username.send_keys("wangwen@outlook.com")

# 输入密码
password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys("123456789qq")

# 点击登录按钮
login_btn = driver.find_element_by_xpath('//*[@id="btn_login"]')
login_btn.click()

# 等待几秒钟
time.sleep(5)

# 断言登录失败的提示语是否存在
driver.find_element_by_link_text("wang5201")
print("测试用例通过了！")

# 退出执行
driver.quit()