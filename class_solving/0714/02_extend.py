a = ['apple']
# a.extend('banana', 'mango') # 오류
a.extend(['banana', 'mango']) # 해결
print(a)

# a.extend('banana')
# print(a)
# ['apple', 'banana', 'mango', 'b', 'a', 'n', 'a', 'n', 'a']
