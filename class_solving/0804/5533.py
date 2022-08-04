# 유니크
from pprint import pprint

list_ = [[100, 99, 98],
         [100, 97, 92],
         [63, 89, 63],
         [99, 99, 99],
         [89, 97, 98]]
score_list = [0] * 5

# pprint(list_)
col_list = []
# 리스트를 90도 회전
for x in range(3):
    col = []
    for y in range(5):
        col.append(list_[y][x])

    col_list.append(col)

# 친구들의 점수 리스트
score_list = [0] * 5
for x in range(3):
    col = col_list[x]
    for y in range(5):
        # 친구의 점수
        score = col[y]
        # 친구의 점수가 리스트에서 1개일 때
        if col.count(score) == 1:
            # 친구의 점수가 증가
            score_list[y] += score
print(score_list)