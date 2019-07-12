
# 怎么来学：学习requests的用法，包括get
# get去服务器获取资源（网页、接口）

# ************************************* 基础内容：掌握 *********************************

# step1. 环境安装：pip3 install requests -i https://pypi.tuna.tsinghua.edu.cn/simple

# step2. 导入requests
import requests

# # step3. 发起请求
# url = "https://www.baidu.com/"  # 网页或者接口的地址
# res = requests.get(url)         # 发起请求并且获得响应值

# step4. 打印响应值
# print(res.text)           # 获取响应信息
# print(res.status_code)      # http状态码



# ************************************** 进阶：掌握 *********************************
url = "http://118.24.29.59:8080/morning/getAllGoods" # 接口地址了
res1 = requests.get(url)

# 解析json值
a = res1.json() # 解析响应信息为字典，接口是返回值必须是json格式的
# print(type(a))    打印解析后的结果的类型
print(a["success"])
print(a["message"])