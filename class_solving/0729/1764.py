# 듣보잡
N, M = list(map(int,input().split()))
print(N, M)
dict_ = dict()
# N의 크기만큼 듣도못한 사람을 입력
for i in range(N):
    p = input()
    dict_[p] = "듣도못한"

list_=[]
# M의 크기만큼 보도못한 사람을 입력
for i in range(M):
    p = input()
    # 입력받은 사람이 딕셔너리의 키 중에 있는가?
    if p in dict_:
        list_.append(p)

list_.sort()
print(len(list_))
for p in list_:
    print(p)
# print(list_)

# 이름을 key로 사용해서 저장할 딕셔너리 변수
# dict_["ohhenrie"] = "듣보잡"
# dict_["charlie"] = "듣보잡"
# dict_["baesangwook"] = "듣보잡"

if "obama" in dict_:
    print("obama 듣보잡")

if "baesangwook" in dict_:
    print("baesangwook 듣보잡")

if "ohhenrie" in dict_:
    print("ohhenrie 듣보잡")

if "charlie" in dict_:
    print("charlie 듣보잡")