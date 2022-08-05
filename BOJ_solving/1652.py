# 누울 자리를 찾아라
import sys

n = int(sys.stdin.readline())

row_count = 0
column_count = 0

matrix = [''] * n

for i in range(n):
    line = input()

    j = 0

    for l in line:
        matrix[j] = matrix[j] + l
        j += 1

    line = line.split('X')

    for l in line:
        if len(l) > 1:
            row_count += 1

for column in matrix:
    line = column.split('X')
    
    for l in line:
        if len(l) > 1:
            column_count += 1

print(row_count, column_count)

'''
참고
https://zoosso.tistory.com/337

'''