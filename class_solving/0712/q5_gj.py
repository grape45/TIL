# 문제 5번
# 주어진 숫자의 평균을 구하는 코드를 작성하시오.
# sum(), len()  함수 사용 금지

# 1. 문제 제공
numbers = [3, 10, 20]
result = 0
for val in numbers:
    result += val
print(result/3)

print('해설 풀이')

# 2. 값 초기화
count = 0

# 3. 반복
for number in numbers:
    result = result + number
    # result += number
    count = count + 1
    # count += 1

print(result/count)
# print(sum(numbers)/len(numbers))