import json

# 파일을 열고,
f = open('stocks.json', 'r', encoding='utf=8')
# JSON을 파이썬 객체 형식으로 한다!
kospi = json.load(f)
samsung = kospi['stocks'][0]
print(samsung, type(samsung))

# stockName, clossPrice 정보만 가진 딕셔너리를 만들고 싶어요 !
result = {
    'stockName' : samsung.get('stockName'),
    'closePrice' : samsung.get('closePrice')
}

# 값을 뽑아서 그냥 출력해주면 된다.
# 실습 4번에 활용
print(result)