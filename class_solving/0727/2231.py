# 분해합
"""

216
"""
# import sys
# sys.stdin = open("분해합.txt")

# 숫자 N 입력
N = int(input())

# 1부터 N 사이의 모든 수의 분해합을 탐색
for number in range(1, N):
    # print(number)
    # 분해합 저장 변수
    split_sum = 0

    # 각 자리수의 합
    for digit in str(number):
        split_sum = split_sum + int(digit)

    # 각 자리수의 합 + 수의 합 => 분해합
    split_sum = split_sum + number

    # 구한 분해합과 입력 N이 같으면
    # number는 N의 생성자
    if N == split_sum:
        print(number)
        # number_list.append(number)
        break # 가장 작은 생성자를 탐색
# for-else
# break를 만나지 않으면
else:
    print(0)

# 생성자가 없을 경우 0을 출력해야한다.

# print(min(number_list))
