# 노드사이의 거리

from collections import deque
n, m = map(int, input().split())
tree = [[0] * (n + 1) for _ in range(n + 1)]
'''
노드 갯수가 적을 때는 인접행렬로도 충분하지만,
노드 수가 많아지면 인접리스트를 이용하는게 효율이 좋다 = 시간복잡도⬇

** 인접행렬 : node와 edge의 정보를 행렬로 표현하는 방법으로, 
edge(연결선)와 상관없이 모든 node를 표현해야 하기 때문에 
node의 수가 많을수록 메모리 사용량이 늘어난다

** 인접리스트 : node와 edge의 정보를 리스트로 표현하는 방법으로, 
연결된 것만 표시하므로 인접행렬에 비해 간단
'''
for _ in range(n - 1):
    x, y, d = map(int, input().split())
    tree[x][y] = d
    tree[y][x] = d

def bfs(start, end):
    q = deque([[start, 0]])
    check = [0] * (n + 1)
    while q:
        s, d = q.popleft()
        if s == end:
            return d
        for i in range(1, n + 1):
            if tree[s][i] != 0 and check[i] == 0:
                check[i] = 1
                q.append([i, d + tree[s][i]])

for _ in range(m):
    s, e = map(int, input().split())
    print(bfs(s, e))