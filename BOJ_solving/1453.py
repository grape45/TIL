# 피시방 알바

n = int(input())  # 손님의 수
client = list(map(int, input().split()))  # 손님이 앉고 싶어하는 자리
cnt = 0  # 자리가 없는 인원
seat = []  # 피시방 자리 생성
for i in range(n):
    if client[i] in seat:         # 앉고 싶어하는 자리에 사람이 있으면
        cnt += 1                  # 거절
    else:                         # 자리에 사람이 없으면 
        seat.append(client[i])    # 앉아서 게임 진행
print(cnt)