import requests

URL = 'https://m.stock.naver.com/api/stocks/marketValue/KOSPI?page=1&pageSize=20'
# URL 주소가 틀렸을 수 있음. 필요에 따라 변경해서 사용

response = requests.get(URL).json()
print(response)