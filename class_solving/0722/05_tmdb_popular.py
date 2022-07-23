import requests
BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
params = {
    'api_key' : 'key입력',
    'language' : 'ko-KR'
}

response = requests.get(BASE_URL+path, params=params).json()
print(response)