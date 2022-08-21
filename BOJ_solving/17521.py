# Byte Coin
# 가격이 올라가면 사서 팔기
# '최종 현금이 매우 커질수 있음을 주의' == type을 int로 받으면 안 될수도? -> int로 해도 통과됨!
# 요일 수 n, 초기 현금 W

from sys import stdin
n, W = map(int, stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(int(stdin.readline()))

c = False # c = 현재 매수 코인이 있는가?
coin = 0 # coin의 개수 cnt
for i in range(n - 1):
    if not c and arr[i] < arr[i + 1]:
        c = arr[i]
        coin = W // c # 나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 수 -> coin
        W -= coin * c

    elif c and arr[i] > arr[i + 1]:
        W += arr[i] * coin
        coin, c = 0, False

if c:
    W += coin * arr[-1]


