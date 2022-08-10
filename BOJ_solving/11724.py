# 연결 요소의 개수

# DFS로 풀이

import sys
sys.setrecursionlimit(10**7) 
#  python은 재귀제한이 걸려있기 때문에 재귀 허용치가 넘어가면 런타임에러 발생. 허용 범위를 넓혀주는 코드임! 
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            visited[i] = True
            dfs(i)

count = 0
for i in range(1, n+1):
    if visited[i] == False:
        count+=1
        dfs(i)

print(count)