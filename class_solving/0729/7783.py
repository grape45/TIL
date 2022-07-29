# 회사에 있는 사람
# import sys
# sys.stdin = open("_회사에있는사람.txt")

'''
4 기록의 수
Baha enter
Askar enter
Baha leave
Artem enter

# Askar
# Artem
'''
N = int(input())
logs = dict()
for i in range(N):
    # 공백으로 나눠진 두개의 단dj
    # print(input().split())
    key, value = input().split()
    logs[key] = value

    # logs["Baha"] = "enter"
    # logs["Askar"] = "enter"
    # logs["Baha"] = "leave"
    # logs["Artem"] = "enter"

# print(logs)

list_ = []
for key in logs:
    print(key)
    # value가 enter인 key를 찾아서 리스트에 저장
    if logs[key] == "enter":
        list_.append(key)

list_.sort
print(list_)