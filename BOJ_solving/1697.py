# 숨바꼭질
# BFS, 1차원 배열, queue
# 선택 가능한 방향 : 총 3가지
'''
1. X-1
2. X+1
3. 2*X
'''

# queue에 넣게 되는 경우 고려사항
'''
1. 시간 정보(몇 초가 흘렀는지)가 들어가야 함
2. 몇 초가 흘렀는지 기록되어 있어야 함
3. 중복 방문을 하지 않음
'''

# 코드 구현은 의외로 간단하나, 접근 방법 및 고려해야 할 사항을 찾는 것이 어려운 문제 (정답률 25%)

# 우열님 코드
from collections import deque
n, k = map(int, input.split())

visited = [0 * (100001)]

queue = deque()
queue.append(n)

while queue:
    cur = queue.popleft()

    if cur == k:
        break

    dis = [cur -1, cur + 1, 2 * cur]

    for d in dis:
        if -1 < d < 100001: # 이 조건이 빠지면 메모리 초과로 런타임 오류 발생
            if visited[d] == 0:
                visited[d] = visited[cur] + 1
                queue.append(d)

print(visited[k])

# https://zidarn87.tistory.com/248
import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())