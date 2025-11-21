a = ()
a = tuple()
print( type(a) )

b = (1,2,3)
print(b)
print(b[0])

# print(b[0]) 에러 - 변경 불가능(readOnly)

c = (1,) # 단 하나의 값을 가지는 튜플의 경우 (값,)로 선언해야 한다.

d = 1, 2, 3, 4 # 괄호를 생략해도 튜플
print(type(d))

