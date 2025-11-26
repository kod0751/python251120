# 내장 함수
# 정수를 문자 하나로 형변환
print('chr(65) :', chr(65))
print('chr(54620) :', chr(54620))

# 문자 하나를 아스키 또는 유니코드로 변환
print('ord("A"):', ord('A'))
print('ord("Z"):', ord('Z'))
print('ord("한"):', ord('한'))


print('int("123"):', int('123'))
print('int("f", 16):', int('f', 16))
print('int("1010", 2):', int('1010', 2))

def pp(x) :
    return x +1
n = [1,2,3,4]
a = map(pp, n)
print('a :', list(a))

def over3(x):
    return x >= 3

b = filter(over3, n)
print('b :', b)
print('list(b) :', list(b))

print("max(n) : ",max(n))
print("min(n) : ",min(n))

income = -100
print(max([income, 0]), '웝 입금 되었습니다')
if income < 0 :
    income = 0
print(str(income) + '원 입금 되었습니다')


users = [
    {
        'id': 'a',
        'level': 12
    },
    {
        'id': 'b',
        'level': 20
    }
]
def get_level(user):
    return user['level']

print(max(users, key = get_level))
print(max(users, key = lambda data : data['level']))


print( 'sum(n) :', sum(n))

print( sorted(n))
n.sort()
print(n)

print( list(reversed(n)))