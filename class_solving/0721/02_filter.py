# 3의 배수인 리스트로만 만들기

numbers = [1, 2, 5, 10, 3, 9, 12]

# 기본 반복/조건 코드
result = []
for n in numbers:
    if n % 3 == 0:
        result.append(n)
print(result)

# 람다 활용
print(list(filter(lambda n : n % 3 == 0, numbers)))

# 함수 활용
def is_3(n):
    return n % 3 == 0

# def is_3_1(n):
#     if n % 3 == 0:
#         return True
#     else:
#         return False

# is_3(n) 과 is_3_1(n)은 동일한 결과를 내는 코드이다.