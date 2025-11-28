# 내장 모듈

# 날짜와 시간
from datetime import datetime, date
now = datetime.now() # 오늘 날짜와 시간
print( now, type(now))
print(now.strftime('%Y년 %m월 %d일 %H시 %M분 %S초'))
print(now.strftime('%Y년 %m월 %d일 %p %I시 %M분 %S초.%f'))

print( now.date()) # 오늘 날짜

start = date(2025, 11, 19)
today = date(2025, 11, 28)
print( today - start)

# 시간
import time
print( time.time()) # 1970년 1월1일 자정 기준으로 지난시간(초 단위)

before = time.time()
# 시간을 측정하고 싶은 코드 작성
for i in range(10):
    #print(i)
    pass
    #time.sleep(0.5) # 일시정지 (초 단위)
after = time.time()
print(f'걸린 시간 : {after - before}')

# 랜덤
import random
print(random.random()) # 0 <= rand <1
print(random.randint(1,6)) # 1 ~ 6 사이의 무작위 정수
a = [1,2,3,4,5]
print(random.choice(a)) # 시퀀스 객체에서 무작위 선택
random.shuffle(a)
print(a)

# JSON
import json
j = '''
    {
        "name": "홍길동",
        "birth": "0525",
        "age": 30
    }
'''

d = json.loads(j)
print(d, type(d))

j2 = json.dumps(d)
print(j2, type(j2))

d2 = {
    'hasCar' : True
}
print('='*50)
print( json.dumps(d2) ,type(d2))
j3 = json.dumps(d2)
print(j3)
print(json.loads(j3) ,type(j3))


import urllib.request as req
response = req.urlopen('http://naver.com')
print(response)
print(response.read().decode('utf-8'))

import webbrowser
webbrowser.open_new('http://naver.com')
webbrowser.open('http://daum.net')

