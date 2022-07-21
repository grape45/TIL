import requests
URL = 'https://api.bithumb.com/public/ticker/ALL_KRW'
response = requests.get(URL).json()
# 1. URL로 요청을 보내고
# 2. 응답(HTML)을 받아서
# 3. 조작!
print(response)