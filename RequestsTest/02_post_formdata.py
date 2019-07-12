
# ******************************************** 基础：掌握：如何用postman生成requests的脚本 ********************************************
# post的form-data格式的请求参数 -- post生成代码

import requests

# 接口地址
url = "http://118.24.29.59:8080/morning/user/userLogin"

# form-data格式的请求参数
payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"user.loginName\"\r\n\r\n2941635995@qq.com\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"user.loginPassword\"\r\n\r\na123456\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"

# 请求头
headers = {
    'User-Agent': "PostmanRuntime/7.13.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "de54f430-5430-4fb7-aaef-f4997b7d801c,fa054b95-af66-44ef-8768-664f7fa79e09",
    'Host': "118.24.29.59:8080",
    'cookie': "JSESSIONID=33C726C0468C83D7200C67E02FC391E4; session=.eJyVUMtuwyAQ_JVqz0YqbpUH5176FRWBLSZgcGGp00T592LhVFVuOaB9DLMzuxcoGROIC0itE-YMAqADaRBEKN53oND7aYgBG6ISSsK3-mrdP_Md4z3rN098I162gvf1C-qiJNkYGgNHaX1LrQbxuq9xNGtjNO_6phSsckGOy2DCTLzik8x5jkn_a6U6L7lGz3haE2uCpJJWk5lqUVfhHVB0uBhBXubDz3ZguD8TQ348Mpf8gRk8l--vk_uMHiuzTPpvveZquc-dqxnVIGmRujb84yGV6y_Kp3ZN.XO0qkQ.7WAUG7qgAACFGu5cIuJZTKQ1GP4",
    'accept-encoding': "gzip, deflate",
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'content-length': "310",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

# 请求并获取响应值
response = requests.request("POST", url, data=payload, headers=headers)

# 打印响应值
print(response.text)