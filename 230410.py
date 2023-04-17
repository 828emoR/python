'''
복습

sum = 0
for i in range(1, 101):
    sum = sum + i
print(f"1에서 100까지의 합은 {sum} 입니다.")
//## 중첩반복문 ##//
for i in range(1, 11):
    for j in range(1 , 11):
         for k in range(1 , 11):
            print(f"{i=} {j=} {k=}" )
i = 2
i2 = 1
for i in range(2, 10):
    print(f"\n<  {i} 단 >")
    for i2 in range(1, 10):
        print(f"{i:2d} * {i2:2d} = {i*i2:2d}  ",end="\n")

    print("")


while True:
    a = int (input(f"100이 되도록 입력 해주세요 \n >"))

    if a == 100:
        print(f"100이 되었습니다. 종료합니다.")
        break
    elif a < 100:
        print(f"100미만입니다. 100이 되도록 수를 입력해주세요.\n >")
        a1 = int(input())
        result = a + a1
        if result == 100:
            print(f"100입니다. 종료합니다.")
            break
        elif result != 100:
            print(f"현재 수는 {result}입니다.")
            if result > 100:
               a2 = int (input(f"100을 초과했습니다. 100이 되도록 뺄 수를 입력해주세요. \n>"))
                r2 = result - a2
               
            elif result < 100:
               a3 = int(input(f"100에 도달하지 못했습니다. 100이 되도록 수를 입력해주세요. \n>"))
    elif a > 100:
        print(f"100이상입니다. 100이 되도록 수를 입력해주세요.\n >")

'''
        
r1 = 0;
while True :
    i = input(f"정수를 입력해주세요")
    if i == "=":
        print("=를 입력하셨습니다. 종료합니다.")
        break
    else:
        r1 += int(i)
        print(f"현재까지의값은 {r1}입니다." )

while True:
    try:
        a = int(input("나누기를 할 정수를 입력하세요:"))
        b = int(input("나누어질 수를 입력하세오"))
        print (a/b)
    except : 
        print("0으로 나눌 수 없습니다 ㅋ")
        break

r1 = 0;
while True :
    i = input(f"정수를 입력해주세요")
    if i == "=":
        print("=를 입력하셨습니다. 종료합니다.")
        break
    else:
        try:
            r1 += int(i)
            print(f"현재까지의값은 {r1}입니다." )
        except:
            print("에러인데수웅")
