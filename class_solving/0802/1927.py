# 최소 힙
# input 핸들링 전
'''
for solving idea
1. 자연수 -> 배열에 넣는 heapq.heappush
2. 0 -> 작은 값 제거 heapq.heappop
'''
import heapq

numbers = [0, 12345678, 1, 2, 0, 0, 0, 0, 32]

heap = []
# heapq.heapify(heap)
# 리스트를 push, pop만 해도 heapif를 명시하지 않아도 돌아감

for number in numbers:
    if number != 0:
        heapq.heappush(heap, number)
    else:
        if len(heap) == 0: # len(heap): 까지 작성해도 동일한 코드
            print(0)
        else:
            print(heapq.heappop(heap)) 
