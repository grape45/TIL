import random

# numbers = random.sample([1, 2, 3], 2)
# print(numbers, type(numbers))

# 1~45까지의 숫자!
# 그 중에 6개
n = int(input('얼마쓸래?'))
for i in range(n):
    numbers_2 = random.sample(range(1, 46), 6)
    numbers_2.sort()
    print(numbers_2)

# print(numbers_2) 들여쓰기를 여기다 하면 n = 5일 때 값이 5개가 안나옴
# 들여쓰기의 중요성