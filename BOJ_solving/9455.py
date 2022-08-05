# 박스 # 디버그 필요, LINE 40, ERROR
box = 1 
blanck = 0

row_count, column_count = 5, 4

box_list = [
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 1, 0, 0],
    [1, 0, 1, 0],
]
distance = 0
# 이중 반복문
# 열부터 순회
for x in range(row_count):
# 행 순회, 단 아래에서 위 방향으로 탐색
#   # 4 -> 0 -1
    for y in reversed(range(row_count)):
        print(y, x)
# 또는
#   for y in list(range(row_count))[::-1]:
#       print(y, x)

        # 만약 현재 탐색하고(보고)있는 좌표에 박스가 있으면
        if box_list[y][x] == box:
d
            # y + 1 -> 5 : 조건 만족 X

            # while y + 1 != row_count and box_list[5][x] != box:
            while True:

                # 범위를 체크 1순위 *********
                if y + 1 != row_count:
                    break

                # 값을 체크 2순위 ***********
                if box_list[y + 1][x] == box: 
                    break

                box_list[y][x] = blanck
                box_list[y+1][x] = box
                y += 1
                distance  += 1

print(distance)