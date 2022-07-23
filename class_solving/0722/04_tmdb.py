# 나의 api_key 입력
# api_key 발급받아서 키 입력하기
# https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>>
import requests
BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/76341'
params = {
    'api_key' : 'key입력',
    'language' : 'ko-KR'
}

response = requests.get(BASE_URL+path, params=params).json()
print(response)