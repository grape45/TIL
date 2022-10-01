# 암기왕

import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
  n = int(input())
  note1 = list(map(int, input().split()))
  note1 = {n:0 for n in note1}
  m = int(input())
  note2 = list(map(int, input().split()))
  for n in note2:
    if n in note1:
      print(1)
    else:
      print(0)