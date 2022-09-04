# 문제
# 아래 코드는 과일의 개수를 구하는 논리적 오류가 있는 코드의 일부분 입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
 

### 오류 코드
# from pprint import pprint

# fruits = [
#     "Soursop",
#     "Grapefruit",
#     "Apricot",
#     "Juniper berry",
#     "Feijoa",
#     "Blackcurrant",
#     "Cantaloupe",
#     "Salal berry",
# ]

# fruit_count = {}

# for fruit in fruits:
#     if fruit not in fruit_count:
#         fruit_count = {fruit: 1}
#     else:
#         fruit_count[fruit] += 1

# pprint(fruit_count)

### Output
# {'Apricot': 1,
#  'Blackcurrant': 1,
#  'Cantaloupe': 1,
#  'Feijoa': 1,
#  'Grapefruit': 1,
#  'Juniper berry': 1,
#  'Salal berry': 1,
#  'Soursop': 1}

from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count = {fruit: 1}
    else:
         fruit_count[fruit] += 1

    pprint(fruit_count)

# 디버깅 전 아웃풋 : {'Salal berry': 1}
# 디버깅 : pprint를 if, else 조건문과 같은 라인으로 들여쓰기 해줌
# pprint로 출력해서 pprint(fruit_count) 시 Apricot 부터 정렬될 것 같은데
# 이 부분은 완전하게 해결하지 못함
