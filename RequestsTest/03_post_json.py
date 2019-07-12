# 传递的参数也是json的情况
import requests


u = "http://118.24.29.59:5000/userLogin/"                       # 接口地址
d = {"username":"test", "password":"test", "captcha":"123456"}  # 传给接口的参数,参数一定要是字典
res = requests.post(url=u, json=d)
print(res.json())