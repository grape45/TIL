A = int(input())
B = int(input())
C = int(input())

mult = str(A*B*C)
count0 = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0

for i in mult:
    if i == '0':
        count0 += 1
    elif i == '1':
        count1 += 1
    elif i == '2':
        count2 += 1
    elif i == '3':
        count3 += 1
    elif i == '4':
        count4 += 1
    elif i == '5':
        count5 += 1
    elif i == '6':
        count6 += 1
    elif i == '7':
        count7 += 1
    elif i == '8':
        count8 += 1
    elif i == '9':
        count9 += 1
        
print(count0)
print(count1)
print(count2)
print(count3)
print(count4)
print(count5)
print(count6)
print(count7)
print(count8)
print(count9)

# for문? while 문? / while문 일 듯
# 0 - 9 까지 몇 개가 포함되었는지 확인
# int가 아닌 Str로 받아서 갯수를 카운팅
# print(A*B*C)