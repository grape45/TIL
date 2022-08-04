# 성지키기
# 대각선을 지나가는게 최소 인원임 (단, m x n matrix에서 m = n 경우에 한함)
# m, n은 50보다 작거나 같은 자연수
# m x n matrix를 순회하면서 .과 X를 인식 -> cnt += 1
# 2차원 배열이 아니라 1차원 배열로 생각한다면?

n, m = map(int, input().split())
matrix = [0] * m
x_is_guard = 0
for _ in range(n):
    f = input()
    for i in range(m):
        if f[i] == 'X':
            matrix[i] = 1
    if 'X' not in f:
        x_is_guard += 1
y = matrix.count(0)
print(max(x_is_guard, y))