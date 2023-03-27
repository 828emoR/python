'''
a = int(input("입력"))

print(f"500원 =>{a // 500}")

a = a % 500

print(f"100원 =>{a // 100}")

a = a % 100

print(f"10원 = >{a // 10}")

a = a % 10

print(f"10원 =>{a // 1}")

a = a % 1


# if 조건문 (py)(if 단독 사용)
# 숫자를 입력 받아 100보다 크면 "100보다 크다"고 출력
a = True
a = int(input("입력"))

if a > 100 :
    print(f"{a}는 100보다 큽니다.")

else : 
    print(f"{a}는 100보다 작습니다.")

#특정 수를 받아 짝수인지 홀수인지 구하라.
a = True
a = int(input("입력"))
a2 = (a%2)

if a2 == 0:
    print(f"짝수입니다")
else:
    print(f"홀수입니다.")     

#조건문(삼항연산자)
#삼항연산자 사용 가능
even_odd = "홀수" if val % 2 == 1 else"짝수"

a = int(input("입력"))
if a == 0: print("해당 수는 0입니다.")
else:
    if a > 0: (f"해당 수는 0보다 큽니다.")
    else : print(f"해당 수는 0보다 작습니다.")


a1 = int(input("1번 수 입력"))
a2 = int(input("2번 수 입력"))

if a2 == a1 :print(f"{a1}와{a2}는 같습니다.")
elif a2 < a1: print(f"{a1}은{a2}보다 큽니다.")
else: print(f"{a2}는{a1}보다 큽니다.")
'''