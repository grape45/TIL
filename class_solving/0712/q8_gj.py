# 문제 8번
# 주어진 리스트 numbers에서 두 번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지

print('해설풀이')
# 주어진 list
numbers = [0, 20, 100, 40]
max_number = numbers[0]
second_number = numbers[0]
# 혹은
# max_number = float("-inf")
# second_number = float("-inf")

# 1. 전체 숫자를 반복
for n in numbers:
    # 만약에, n이 최대보다 크다면
    if max_number < n:
        # 최댓값이었던 것이 두 번째로 큰 수
        secound_number = max_number
        max_number = n  
    elif second_number < n <max_number: # 이 식이 지원 안되는 언어도 있음 !
    # elif second_number < n and n < max_number # 지원이 안되는 언어들은 이렇게 !
        second_number = n
print(second_number)