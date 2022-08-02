# 최소 힙
'''
for solving idea
1. 자연수 -> 배열에 넣는 heapq.heappush
2. 0 -> 작은 값 제거 heapq.heappop
'''
import heapq

N = int(input())

for _ in range(N):
    n = int(input())

# numbers = [0, 12345678, 1, 2, 0, 0, 0, 0, 32]

heap = []
# heapq.heapify(heap)
# 리스트를 push, pop만 해도 heapif를 명시하지 않아도 돌아감

for number in numbers:
    if number != 0:
        heapq.heappush(heap, number)
    else:
        if len(heap): # len(heap) == 0: 과 같지만, == 0: 은 생략해도 참이 된다.
            print(0)
        else:
            print(heapq.heappop(heap))
