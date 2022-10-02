# 추월

import sys
input = sys.stdin.readline

N = int(input())
police1 = [input().rstrip() for _ in range(N)]
check = {car: False for car in police1}
police2 = [input().rstrip() for _ in range(N)]

idx = 0
cnt = 0
for last in police2:
    while check[police1[idx]]:
        idx += 1
    if last == police1[idx]:
        idx += 1
    else:
        cnt += 1
    check[last] = True
print(cnt)