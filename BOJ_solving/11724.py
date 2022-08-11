# 연결 요소의 개수

# 깊이우선탐색(DFS)으로 풀이
# 연결 요소 : 연결 되어 있는 정점(노드)들을 한 구역으로 보고, 그 구역에 있는 개수를 count

import sys
sys.setrecursionlimit(10**7)
#  python은 재귀제한이 걸려있기 때문에 재귀 허용치가 넘어가면 런타임에러 발생. 허용 범위를 넓혀주는 코드임! 

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1) # 방문 처리 리스트 생성

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs_(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            visited[i] = True
            dfs_(i)

count = 0
for i in range(1, n+1):
    if visited[i] == False:
        count+=1 # DFS가 진행되면서 한 구역의 DFS를 시작할 때마다 연결요소 count 해줌
        dfs_(i)

print(count)