import requests
order_currency = 'ALL'
payment_currency = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
response = requests.get(URL).json()
coins = response.get('data')

# coins : 딕셔너리
# key : coin 이름
# value : 딕셔너리(코인의 정보)
for coin in coins:
    # coins.get(coin) <- 코인의 정봉니 딕셔너리
    # 그 딕셔너리의 closing price
    if coin == 'data':
        continue
    print(coin, coins.get(coin).get('closing_price')) ------- 카카오개발자 페이지 들어가기 전 str 'get' 부분만 다시 돌려 보기