# 지뢰찾기
# 코드 재확인 후 완성하기
import sys

# sys.stdin = open("_questmine.txt")
# from pprint import pprint

# 짧은 리스트는 pprint 출력이 안되므로,
# 아래왁 같이 정의해준다
def pprint(list_):
    for row in list_:
        print(row)

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

mine = "*"
blank = "."

n = 8
gameboard = [
    "...**..*",
    "......*.",
    "....*...",
    "........",
    "........",
    ".....*..",
    "...**.*.",
    ".....*..",
]

openboard = [

]

resultboard = [
for i in range(8):


]

gameboard = list(gameboard)
openboard = list(openboard)
find_mine = Flase

# 이중반복문
for y in range(8):
    for x in range(8):
        # 현재 위치가 오픈한 위치
        # openboard -> x
        if openboard[y][x] == "X":
            mine_count = 0
            for d in range(8):
                quest_y = y + delta_y[d]
                quest_x = x + delta_x[d]
