matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 0, 1, 2]
]

# n x m
n = len(matrix)
m = len(matrix[0])

total = 0

# 방법 1
for i in range(n):
    for j in range(m):
        total += matrix[i][j]
print(total)

# 방법 2
for row in matrix:
    total += sum(row)
# O(n^2)

print(total)

def matrix_sum(matrix):
    return sum(map(sum, matrix))

matrix_sum(matrix)
# O(n^2)

# 방법 3
for row in matrix:
    sum(row)
print(total)