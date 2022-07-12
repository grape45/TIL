# 문제 7번
# 주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.
# min() 함수 사용 금지

# 주어진 list
numbers =[0, 20, 100]
for val in numbers:
    if numbers[0]<numbers[1] and numbers[0]<numbers[2]:
        print(numbers[0])
        break
    elif numbers[1]<numbers[0] and numbers[1]<numbers[2]:
        print(numbers[1])
        break
    else:
        print(numbers[2])
        break

# 한계점
# 리스트가 3개 초과하면 코드 수정해야함. 코드 수정 없이 더 큰 리스트도 수용 가능한 코드?