'''
print(2+3)
print("kim")
print(2+3, "kim")
#a = 3+4
a = "dd"
age =26
print(a)
# print(type(a))

i_name="kim"
f_name="juHwan"
print("kim's age is",  age)
print("his full name is", i_name, f_name, "and his age is", age)
print("오늘 배운것 = 변수선언+str, int 타입 출력")

if a : str(
        print("a's type is string")
)

# ------------230320---------------

# 변수의 타입= 정수형, 실수형으로 나눔.
# 정수형: a = 12345. print(a, type(a))
# 실수형: b = 12345.6789 print(b, type(b))
# 형변환시 int()또는 float()를 사용함.
          
a = 12345
print(a, type(a))

b = 12345.6789
print(b, type(b))
# 정수형& 실수형.

hex = 0xF5A
oct = 0o567
bin = 0b11011
print(hex, oct, bin)

#논리형(Booleaen, 불형)
# true 또는 false값
# bl = true
# print(bl, type(bl))
# a = 10 < 20
# b = 10 == 10
# c = 10 != 10
# print(a,b,c)


bl = True
print(bl, type(bl))


a = 10 < 20
print(a)

b = 10 == 10
c = 10 != 10
print(a,b,c)


print("따옴표 '  출력")
print('따옴표 " 출력 ')
print("같은 따옴표\" 출력")

# 그렇다면 "10 + 20 + 30" 은 어떻게 출력할까?
a = 10
b = 20

# 해답은 아래와 같다.
print(a, "+", b, "=", a+b)


#위와 같은 결과를 도출하는데에는 아래 방식도 가능하다.
a = 10
b = 20 
print("%d" % a)
print("%d" % (a+b))
print("%d + %d = %d" %(a, b, a+b))


int = 12345
float = 12345.6789
print("%10d" % int)
print("%10.4d" % int)

print("%10.4f" % float)
print("%20.10f" % float)
print("%5.5f" % float)
print("%5.2f" % float)
print("%3.2f" % float)




a = 10
b = 20 
print (a,"+",b,"\n =",a+b) 

#print(a,"\b+",b,"\n=",(a+b)) || 10+20=30을 출력하고싶다. 공백을 지우는방법을 알아보자.


a = int (input("첫번째 정수를 입력하세요 : "))
b = int (input("두번째 정수를 입력하세요 : "))

c = a + b

print(c)
print("두 정수를 더한 값은" ,c, "입니다.") #basic
print("두 정수를 더한 값은 %d 입니다." % c) # %d를 이용한 출력
print(f"두 정수를 더한 값은 {c} 입니다.") # f-string을 이용한 출력식.

# 셀프 문제 타임
a = input()
b = input()

print(a, "+", b, "=", a+b)

# a = input()
# b = input()
# print(a, "+", b, "=", a*b)
'''

a = int(input("입력값 a 입력"))
b = int(input("입력값 b 입력"))

a1 = (a+b)
a2 = (a-b)
a3 = (a*b)
a4 = (a/b)

print(f"두 수를 더한 결과값은",{a1},"이며,")
print(f"두 수를 뺀 결과값은",{a2},"이며,")
print(f"두 수를 곱한 결과값은",{a3},"이며,")
print(f"두 수를 나눈 결과값은",{a4},"입니다.")