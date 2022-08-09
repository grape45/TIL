# 얼마?
'''
2
10000
2
1 2000
3 400 # output : 13200
50000
0 # output : 50000
'''

tc = int(input())

for _ in range(tc) :
  s = int(input())
  n = int(input())
  if n == 0 :
    print(s)
  else :
    option = 0
    for _ in range(n):
      q, p = map(int, input().split())
      option += q * p

    print(s + option)