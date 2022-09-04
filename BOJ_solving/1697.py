# 숨바꼭질
# BFS, 1차원 배열, queue
# 선택 가능한 방향 : 총 3가지
'''
1. X-1
2. X+1
3. 2*X
'''

# 들어가기 전 stack, queue, deque 간단 복습
'''
1. stack
- 차곡차곡 쌓아 올린 자료구조
- "같은 구조와 크기의 자료를" 쌓음
- top으로 정한 곳을 통해서 push나 pop으로 접근 가능
- LIFO(Last In First Out)
- 활용 예 : 웹페이지 뒤로가기, 실행 취소(undo), 수식 괄호 검사 등
- 장점 : 구현이 쉬움, 원하는 데이터의 접근 속도가 빠름
- 단점 : 데이터 최대 개수 미리 지정 필요, 데이터 삽입 및 삭제가 비효율적임

2. queue
- 한쪽에서 삽입(rear), 다른쪽에서 삭제(front) 작업 가능
- 데이터가 들어올 때는 rear, 나갈 때는 front
- 접근 방법이 가장 첫 원소와 끝 원소 모두 가능함
- FIFO(First In First Out)
- 활용 예 : 우선순위가 같은 작업, 은행 업무(대기번호), 프로세스 관리(운영체제의 작업 스케줄링),
            BFS 구현, 캐시 구현
- 장점 : 데이터가 입력된 시간 순서대로 처리해야 할 경우 유리함
- 단점 : 크기가 제한적, 큐의 앞부분이 비어도 데이터 삽입 불가, 큐가 비어있어도 not empty로 판단할 수 있음(rear가 맨 뒤)

3. deque
- 삽입과 삭제가 리스트의 양쪽 끝에서 모두 발생 가능
- deque = double ended queue
- stack과 queue의 장점만 따서 구성
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
visited = [0] * 200001

queue = deque()
queue.append(n)

result = 0
while queue:
    next = queue.popleft()