# 두 수를 Input으로 받아 합을 구하는 코드이다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# 문제
# numbers = input().split()
# print(sum(numbers))

# input : 10 20
# output : 30

# numbers1 = int(input())
# numbers2 = int(input())
# print(numbers1 + numbers2)

# 오류 원인 : 입력 및 출력하고자 하는 type에 대한 고려가 없었음
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# split()은 str을 나누는건데, out은 int를 받으려고 함