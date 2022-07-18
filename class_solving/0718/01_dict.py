word = 'banana'
result = {}
for char in word:
    # result[char] : 없으면 KeyError
    # result.get(char, 0) # 없으면 None, 기본값을 주면 0
    result[char] = result.get(char, 0) + 1


print(result)