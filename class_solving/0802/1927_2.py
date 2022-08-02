# 최소 힙
# input 핸들링 후

import heapq

heap = []

for _ in range(int(input())):
    n = int(input())

    if n != 0:
        heapq.heappush(heap, n)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))