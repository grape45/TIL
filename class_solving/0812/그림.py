# 코드 확인하고 보완하기

def pprint(arr):
    for i in range(len(arr)):
        print(arr[i])

dy = [-1, 0, 1, 0]
dx = [0, 0, 0, 0]

visited = []

for _ in range(n):
    # boolean(False) 가 m개인 일차원 그래프?
    visited_list = [False] * m
    visited.append(visited_list)

# 모든 좌표에서 DFS 로직 실행
# 이차원 리스트를 순회할 이중 반복문
for y in range(n):
    for x in range(m):
        # [y, x] 값이 1이고, 방문하지 않았다면
        # DFS 실행
        if not visited[y][x] and graph[y][x] == 1:
            stack = []
            stack.append([y, x])
            visited[y][x] = True

            while len(stack) != 0:
                node = stack.pop()

                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]

                    # 조건 1, 2, 3
                    # 조건 1. 범위 조건
                    if not (-1 < ny < n and -1 < nx < m):
                        continue

                    # 조건 2. 방문 확인
                    # 방문을 했던 좌표라면
                    if visited[ny][nx] == True:
                        continue

                    # 조건 3. 좌표의 값이 1
                    # 그림이어야 한다
                    if graph[ny][nx] != 1:
                        continue

                    # 조건을 다 통과하면
                    # stack 다음 좌표 넣고,
                    # 방문 처리
                    stack.append((ny, nx))
                    visited[ny][nx] = True