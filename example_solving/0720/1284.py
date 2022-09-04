import sys
from xml.etree.ElementTree import QName
sys.stdin = open("1284_input.txt", "r")

# A사 : 1L * P원
# B사 : 
# R이하 : Q
# R초과 : Q + S*(W-R)


T = int(input())
for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    print(P, Q, R, S, W)
    # print(P, Q, R, S, W)
    A = W * P
    if R > W:
        B = Q
    else:
        B = Q + S*(W-R)
    print(f'#{test_case} {min(A, B)}')