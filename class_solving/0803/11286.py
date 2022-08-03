# 절대값 힙

from heapq import *
N = 18
heap = []
X = [1, -1, 0, 0, 0, 1, 1, -1, -1, 2, -2, 0, 0]
# x = int(input())

# heappop 값을 뺄 때
root = heappop(heap)
print(root[1])

# heappush 값을 넣을 때
heappush(heap, [abs(x), x])

# Q. 파이썬 heap은 최소 heap을 의미,
# 최대 heap으로 이 문제를 푼다면?