# 예제 07. [오류 해결] 평균 구하기
# 아래 코드는 평균을 구하는 논리적으로 오류가 있는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# 오류 코드
# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# total = 0
# count = 0

# for number in number_list:
#     total += number
# count += 1

# print(total // count)

### Output
# 5.5

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 10

for number in number_list:
    total += number
# count += 1

print(total / count)

# 오류 수정 전 output : 55
# 오류 코드 상으로는 count += 1 까지 안 돌아감
# count = 10 으로 고정시키고 total // count 가 아닌 total / count 로 output 값은 도출함
# 출제 의도는 count += 1 이 작동시키는 것으로 판단됨 