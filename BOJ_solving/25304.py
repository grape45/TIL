# 영수증

import sys

input = sys.stdin.readline

# 총 구매가격과 실 구매가격이 동일한지 확인
def receipt(total_price, purchase_price):
    return 'Yes' if total_price == sum([i[0] * i[1] for i in purchase_price]) else 'No'

if __name__ == '__main__':
    i = int(input())  # total_price
    n = int(input())  # purchase_price
    purchase_price = [list(map(int, input().split())) for _ in range(n)]

    print(receipt(i, purchase_price))