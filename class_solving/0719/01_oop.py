word_list =['abc', 'banana', 'apple']

def transform_uppercase(word):
    result = ''
    for char in word:
        number = ord(char)
        number = number-32
        result += chr(number)
    return result

for word in word_list:
    print(transform_uppercase(word))




my_list = [1, 2, 3]
# 리스트.sort()
# 리스트의 데이터를 직접 정렬
my_list.sort()

my_list = [1, 2, 3]
# 리스트는 sorted 함수의 인자로 전달될 뿐.
sorted(my_list)