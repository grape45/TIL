# 다이얼
dict_ = {
    "A": 2, "B": 2, "C": 2,
    "D": 3, "E": 3, "F": 3,
    "G": 4, "H": 4, "I": 4,
    "J": 5, "K": 5, "L": 5,
    "M": 6, "N": 6, "O": 6,
    "P": 7, "Q": 7, "R": 7, "S": 7,
    "T": 8, "U": 8, "V": 8,
    "W": 9, "X": 9, "Y": 9, "Z": 9 
}

# 시간을 저장할 변수
time_ = 0

string = "UNICIC"
for key in string:
    # 딕셔너리 변수에 key로 접근
    number = dict_[key]
    print(key, number)
    time_ += number + 1
print(time_)

'''
for문으로 푸는 방법
for key in string:
    if key == "A":
        number = 1
        if key in ["A", "B", "C"]:
            ...
'''