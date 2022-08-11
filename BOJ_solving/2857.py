# FBI

who_FBI = []  
for i in range(1, 6):  # 5명의 요원만 check하니까
    n = input()  
    if "FBI" in n:
        who_FBI.append(i)
if who_FBI:  
    print(*who_FBI)  
else:  
    print("HE GOT AWAY!")