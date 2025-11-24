a = 0
while a < 5 :
    print(a)
    a += 1
print('>>>', a)

# 반복 휫수를 잘 모를떄 while
# 반복 휫수를 정확히 알때 for

money = 300
while True :
    print('남은 금액:', money)
    money -= 100

    if money <= 0 :
        break


count = 10
while count > 0 :
    count -= 1
    # if count % 3 != 0 : # 3의 배수가 아닐떄 
    #     print(count)
    if count % 3 == 0 : # 3의 배수일때
        continue
    print(count)


count = 0 
while count < 5 :            # 무언가 찾을 때 사용
    count += 1
    if count == 2 :
        break
    print(f'카운트: {count}')
    
else : # while이 조건에 의해 종료 될 때 실행
       # 즉, break를 안만나면 else가 실행된다
    print('break 안만남')

# while ~ else 이해를 높여보자
# 0~9 사이에 7이 있는지를 찾아보자
n = 7 # 찾을 값
i1 = 0
i2 = 9
isFound = False

while i1 < i2 :
    if i1 == n :
        print('찾음')
        isFound = True
        break
    i1 += 1
if not isFound : 
    print('못 찾음')

while i1 < i2 :
    if i1 == n :
        print('찾음')
        break
    i1 += 1
else :
    print('못 찾음')

    