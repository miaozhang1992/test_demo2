import requests

# 发送GET请求
response = requests.get('https://api.example.com/data')

# 打印响应状态码
print(response.status_code)

# 打印响应内容
print(response.text)
