import time
from selenium import webdriver

# selenium + pytest的执行方法
# 一定要去终端里面使用pytest xxx.py的命令来运行，不要再用python xxx.py的命令运行了！！！
def test_morning():
    driver = webdriver.Chrome(executable_path="C:\\Users\\SNake\\VSCodeProjects\\ljtest201906\\SeleniumTest\\chromedriver.exe")
    driver.maximize_window()
    driver.get("http://118.24.29.59:8080/morning/")
    
    driver.find_element_by_link_text("登录").click()
    driver.find_element_by_id("adminNo").send_keys("test@qq.com")
    driver.find_element_by_id("password").send_keys("a123456")
    driver.find_element_by_id("btn_login").click()

    time.sleep(3)

    e = driver.find_element_by_link_text("test")
    assert e is not None
    print("测试通过！")

    driver.quit()


def test_baidu():
    print(1+1)
    