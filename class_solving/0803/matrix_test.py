# 3 x 3 크기의 입력을 받기
'''
1 2 3
4 5 6
7 8 9
'''
from pprint import pprint
matrix = []

for _ in range(3):
  line = list(map(int, input().split()))
#   line = list(input())
# list로 출력 시 character 단위로 출력 됨
  matrix.append(line)

pprint(matrix)

# Expression by List Comprehension
matrix = [list(map(int, input().split())) for _ in range(3)]