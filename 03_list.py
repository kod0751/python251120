a = 'abc'
print(type(a))
print(1, a.strip())

a=[]
a = list()
print(type(a))
#print(2, a.strip())

a = [1, 2, 3]
print(a)
print(a[-1])


a = [1, 2, 3, 4, 5]
print(a[0:2])

b = 'abcde'
print(b[1:4])

print(a[:2])
print(a[1:])
print(a[1:100]) # 초과되도 리스트 끝까지만 출력

c = [1,2,3,4,5,6,7,8,9]
print(c[5:2])
print(c[1::2])

print(len(c))

a = [1,2,3,4,5]
del a[1]
print(a)

b = [1,2,3,4,5,6]
del b[1:3]
print(b)

a.append(60) # 마지막에 붙는다
print(a)
a.append([100,200])
print(a)

d = [123,224,45,31,68,94]
d.sort()
print(d)

d.reverse()
print(d)

list1 = d.sort()
print(list1) # None

e = [1,2,3,4,5,6]
print(e.index(3))
# print(e.index(30)) # error
# print(e.find(3)) # error
print( 3 in e ) #true

e.insert(3,5)
print(e)

f = [1,2,3,4,3]
f.remove(3) # 왼쪽부터 해당 값 하나만 삭제
#f.remove(50) # 값 없을경우 에러
print(f)

g = [1,2,3,4]
h = g.pop() # 마지막 것을 빼서 돌려줌
print(g, h)

i = [1,2,3,3]
j = i.count(3)
print(j)

i.extend([10,20])
print(i)
i += [100,200]
print(i)