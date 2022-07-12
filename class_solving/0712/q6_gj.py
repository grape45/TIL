# 문제 6번
# 주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.
# max() 함수 사용 금지

# 주어진 list
numbers = [0, 20, 100]
for val in numbers:
    if numbers[0]<numbers[1] and numbers[1]>numbers[2]:
        print(numbers[1])
        break
    elif numbers[1]<numbers[0] and numbers[0]>numbers[2]:
        print(numbers[0])
        break
    else:
        print(numbers[2])
        break

# 한계점
# 리스트가 3개 초과하면 코드 수정해야함. 코드 수정 없이 더 큰 리스트도 수용 가능한 코드?

print('해설풀이')
# 최댓값 구하기
# numbers = [0, 20, 100, 40]
max_num = numbers[0] # 첫 번째 값을 주고 시작함 # 보통은 float("-inf")
# 1. 반복
for n in numbers:
    # 2. 만약, max값이 n보다 작으면 바꾼다
    if max_num < n:
        max_num = n
print(max_num)