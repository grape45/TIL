# 인사성 밝은 곰곰이

N = 7
gom = 0
log_list = [
    "ENTER",
    "pjshwa",
    "chansol",
    "ENTER",
    "pjshwa",
    "chansol",
]

set_ = set()
for log in log_list:
    if log == "ENTER":
        set_.clear()

    else:
        # 닉네임 = log
        # list에서 중복 탐색 시 O(N) 만큼의 시간이 필요
        # 반면 set에서 중복 탐색 시 O(1) 만큼의 시간이 필요
        if log not in set_:
            set_.add(log)
            gom += 1

print(gom)