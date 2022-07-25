import requests
order_currency = 'ALL'
payment_currency = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
response = requests.get(URL).json()
coins = response.get('data')

# coins : 딕셔너리
# key : coin 이름
# value : 딕셔너리(코인의 정보) <-
for coin in coins:
    # coins.get(coin) <- 코인의 정보인 딕셔너리
    # 그 딕셔너리의 closing price
    if coin == 'date':
        continue
    print(coin, coins.get(coin).get('closing_price')) 


# AttributeError: 'str' object has no attribute 'get'
# 사용한 데이터 어딘가에  'str' object가 있어서 발생한 오류
# coins 가 문자열이었거나 coins.get(coin)이 문자열이었거나 둘 중 하나 
 