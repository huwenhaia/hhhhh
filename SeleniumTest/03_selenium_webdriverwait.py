# ************************** 进阶：能掌握就掌握，不能掌握也没有关系


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://118.24.29.59:8080/morning/")

# 动态查找元素的好处
locator = ("xpath", '//*[@id="mian-nav-right-login"]/a[1]')
e = WebDriverWait(driver, 30).until(lambda s: s.find_element(*locator))
e.click()