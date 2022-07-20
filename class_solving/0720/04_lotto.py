import random

print('졸부가 되고 싶어 1')
numbers = range(1, 46)
result = random.sample(numbers, 6)
result.sort()
print(result)

numbers = range(1, 46)
result = random.sample(numbers, 6)
result.sort()
print(result)

numbers = range(1, 46)
result = random.sample(numbers, 6)
result.sort()
print(result)

numbers = range(1, 46)
result = random.sample(numbers, 6)
result.sort()
print(result)

numbers = range(1, 46)
result = random.sample(numbers, 6)
result.sort()
print(result)


print('졸부가 되고 싶어 2')
for i in range(5):
    numbers = range(1, 46)
    result = random.sample(numbers, 6)
    result.sort()
    print(result)


print('졸부가 되고 싶어 3')

# n을 넣으면
# 그 횟수만큼 
def generate_lotto(n):
    result = []
    for i in range(n):
        numbers = range(1, 46)
        result = random.sample(numbers, 6)
        result.sort()
        print(result)

print(generate_lotto(5))