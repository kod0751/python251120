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



