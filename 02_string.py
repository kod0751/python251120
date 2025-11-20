print("hello")
print('"world"')
print(""" hello world """) # Enter가능 (범위)

print(" 나는 \"이름\" 입니다 ")

print('''
    글씨1
    글씨2
    글씨3
''')

print('''
    글씨1\
    글\t씨2
    글\n씨3
''')

print(1,2,3)

print('처음' + '다음')
# print(1 + '다음')
# print(1 + '2')

print(str(1) + '글씨')

print('-' *30)

a = 'abcde'
print( a, len(a))

a = 14
b = '오늘의 온도는' + str(a)+ '도입니다'
print(b)

c = f"지금 기온은 {a}도 입니다"
print(c)

e = '지금 기온은 %d도 입니다' % a
print(e)

print('%4d' % 0)

f = '오늘: {0}일, 내일: {1}일'.format(20, 21)
print(f)

a = 'hobby'
print(a.count('b')) # b가 몇 번 들어가 있는지 세줌

print(a.find('b')) # 최초로 만나는 index 반환
print(a.find('x')) # 없으면 -1
#index()도 비슷하지만 없으면 에러

b = 'abcde'
c = ':'

print(c.join(b))
print(",".join(b))

a = " h i     "
print(a.strip())

a = 'hobby'
b = a.replace('b', '!')

print(b)

a = "Life is too short"
b = a.split(' ') # 글씨를 배열로 만들어 줌
c = a.split() # 전달인자 없는 경우 기본값 공백
print(a,b,c)
d = a.split('i')
print(d)


a = 'https://naver.com'
print( a.startswith('https'))
print( a.endswith('.net'))