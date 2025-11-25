test_list = ['a', 'b', 'c']
for letter in test_list :
    print(letter)

for letter in 'hello' :
    print(letter)

print(letter)

d = {
    'a': 'aa',
    'b': 'bb',
    'c': 'cc'
}

for key in d :
    print(key, d[key])

d.keys()
d.values()
d.items()
# for (k,v) in d.items()
for k, v in d.items() :
    print(f'k : {k}, v: {v}')


r = range(5)
print('range(5) :', r)

r = range(0, 5)
print('range(0, 5) :', r)
print( list(r))
# range (시작숫자, 종료숫자+1, 건너뛰기)

for i in range(0, 5) :
    print(i)

print('-' * 20)
for i in range(2, 5) :
    print(i)

print('-' * 20)
for i in range(2, 10, 3) :
    print(i)

print('-' * 20)
for i in range(10, 2, -1) :
    print(i)


print('-' * 20)
# 1부터 100까지 모두 더한 값 출력
sum = 0
for i in range(1, 101):
    sum += i
print(sum)

# 1~100까지 3또는 5의 배수는 제외하고 모두 더하기
answer = 0
for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0 :
        continue
    answer += i 
print(answer)

answer = 0
for i in range(1, 101) :
    if i % 3 != 0 and i % 5 != 0 :
        answer += i
print(answer)


print('-' * 20)
arr = [51, 52, 53, 54, 55]
idx = 0
for value in arr :      # value만 사용할 때
    print(idx, value)
    idx += 1
    
for i in range( len(arr) ) :  # index가 필요할 때
    print(i, arr[i]) 

print('-' * 20)
## 구구단 출력

for i in range(2, 10) :
    print(f'{i}단 ', end='')
    for j in range (1, 10) :
        print(f'{i}X{j} = {i*j}  ', end='')
    print('')


for i in range(5) :
    print(i)
else :
    print('break 안만남')

for i in range(5) :
    print(i)
    break
else :
    print('break 안만남')

#############################
# 리스트 컴프리헨션 comprehesion
print('리스트 컴프리헨션')
print('='*20)

for i in range(1,10) :
    print(i)

# 1~9 값을 가지는 리스트를 쉽게 만들어보자
a = []
for i in range(1,10) :
    a.append(i)
print(a)

print('='*20)
a = [i for i in range(1,10) ]
print(a)

# 17의 배수 5개
b = []
for i in range(1, 6) :
    b.append(i*17)
print(b)

b=[]
for i in range(17, (17*5)+1, 17) :
    b.append(i)
print(b)

b=[]
b = [i*17 for i in range(1,6)]
print(b)

b=[]
b = [ i for i in range(17, (17*5)+1, 17)]
print(b)

## 3의 배수 - (3,6,9)
c = []
for i in range(1, 10) :
    if i % 3 == 0 :
        c.append(i)

for i in range(3, 10, 3) :
    c.append(i)
print(c)

c = [i for i in range(1,10) if i % 3 == 0]
print(c)

# 3과 5의 배수
c = []
for i in range(1, 10) :
    if (i % 3 == 0) or (i % 5 == 0) :
        c.append(i)
print(c)

c = [ i for i in range(1,10) if (i % 3 == 0) or (i % 5 == 0)]
print(c)

# 1~9까지에서
# 홀수는 그대로
# 짝순는 2배인 배열을 만들자

d = []
for i in range(1,10) :
    if i % 2 == 0 :
        d.append(i*2)
    else :
        d.append(i)
print(d)

d=[i*2 if i % 2 == 0 else i for i in range(1,10)]

print('='*20)
## 구구단
e = []
for i in range(2,10) : # 바깥쪽
    for j in range(1, 10) : #안쪽
        e.append(f'{i}X{j}={i*j}')
print(e)
print('='*20)
f = [[f'{i}X{j}={i*j}' for j in range(1,10)] for i in range(2,10)]
print(f)

print('='*20)
g = [f'{i}X{j}={i*j}' for i in range(2, 10) for j in range(1, 10)]
print(g)

print('='*30)
# 딕셔너리 컴프리헨션
a = {}
for i in range(5) :
    a[i] = i ** 2
print(a)

a = { i:i ** 2 for i in range(5) if i % 2 == 0}
print(a)

print('='*20)
a = [11,12,13,14]
for i, data in enumerate(a) :
    print(i, data)

print('='*20)
a = [11,12,13,14]
for i, _ in enumerate(a,1) :
    print(i, _)

print('='*20)
a=[1,2,3]
b=[7,8,9]
c = zip(a, b)
print(c)
d = list(c)
print(d)


lang = 'Kor'
kr = ['소개', '채용']
en = ['About', 'Recruit']

# # '소개'를 출력
# if lang == 'Kor' :
#     print(kr[0])
# elif lang = 'Eng' :
#     print(en[0])


'''
문제1
1~n 까지 짝수의 합을 구하기

문제2
1~n 까지 숫자를 3개씩 옆으로 찍기

문제3
+++*---
++***--
+*****-
*******

문제4 
주사위 2개를 굴려서 중복을 제거한 경우의 수
[1,2] [2,1] : 중복이라서 하나로 보기

문제5
키오스크 처럼 메뉴 2개와 종료 'x' 문자를 받아서
'x'가 입력되기 전까지 무한반복
1: 아아 , 2: 라뗴, x: 종료'
'''
print('='*20)
# 문제 1
n = 10
sum=0  
for i in range(1,n+1) :
    if i % 2 == 0 :
        sum += i
print(sum)


print('='*20)
# 문제 2
n = 24
for i in range(1,n+1) :
    print(i, end=' ')

    if i % 3 == 0 :
        print('')

print('='*20)
# 문제 3
n = 4 # 1 3 5 7
for i in range(1, n+1) :
    plus = '+' * (n - 1 - (i-1))
    mul = '*' * (2 * (i-1) + 1)
    miu = '-' * (n - 1 - (i-1))
    print(plus + mul + miu)

print('='*20)
# 문제 4
arr = []
num = 0
for i in range(1, 7) :
    for j in range(i, 7) :
        arr.append([i,j])
print(len(arr))       
        

print('='*20)
# 문제 5
prompt = '''
1. 아아
2. 라떼
3. x
'''

