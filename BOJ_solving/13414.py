# 수강신청

import sys
input = sys.stdin.readline
K, L = map(int, input().split())
queue_list = {}

for i in range(L):
    studentId = input().rstrip()
    queue_list[studentId] = i

cnt = 0
for x in sorted(queue_list.items(), key=lambda x: x[1]):
    cnt += 1
    if cnt > K:
        break
    print(x[0])