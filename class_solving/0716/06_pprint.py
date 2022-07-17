from pprint import pprint

pprint({
    'a' : 'apple',
    'b' : [
        'banana',
        'baby'
    ],
})

print({
    'a' : 'apple',
    'b' : [
        'banana',
        'baby'
    ],
})

# 딕셔너리 항목이 두 개라 그렇지만
# 딕셔너리 활용 시 좀 더 편하게 볼 수 있는게 pprint 임
# 알파벳 순으로 정렬시켜줌
# 딕셔너리는 원래 순서가 없지만 정말 가독성을 목적으로 함
# 가독성 측면에서 사용할 가치가 있다