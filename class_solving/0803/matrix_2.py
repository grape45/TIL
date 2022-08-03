from pprint import pprint

# for _ in range(n):
#     matrix.append([0] * m)

# n x m
# n : 행의 개수
# m : 열의 개수
n = 10
m = 10

# n = 10
# m = 4

matrix = [[0] * m for _ in range(n)]

print(matrix)

pprint(matrix)