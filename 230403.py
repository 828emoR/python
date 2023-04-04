'''
a = int(input("성적을 입력하세요"))

if a >= 90:
    print(f"당신의 점수는 {a}점이며, 학점은A입니다.")
elif a >= 80 :
    print(f"당신의 점수는 {a}점이며, 학점은B입니다.")
elif a >= 70 :
    print(f"당신의 점수는 {a}점이며, 학점은C입니다.")
elif a >= 60:
    print(f"당신의 점수는 {a}점이며, 학점은D입니다.")
elif 59 >= a :
    print(f"당신의 점수는 {a}점이며, 학점은F입니다.")

# 구조적 패턴 매칭
# match subject
    case <pattern_1>
        statement1
    case <pattern_1>
        statement1
...
case_   #called wildcard
    statement_default


i = int(input("점수를 입력하세요:"))
print(i)
i = i//10
# "//"를 쓰기 싫다면 i = int(i/10) 을 해도 된다.
match i:
    case 10:
        print('A')
    case 9:
        print('A')
    case 8:
        print('B')
    case 7:
        print('C')
    case 6:
        print('D')
    case _:
        print('F')

for a in range(23):
    print(a)
   
for a in range(6, 23):
    print(a)
    print(a+6)
    print(a//5)

for i in range (5):
    print("*")

for i in range (5):
    print("*", end="*")

a = 0

for i in range (1, 101):
    a += i
print(a)
 
a = int(input("수를 입력하세요"))

# for a in range (1, 10):
#     print("")
for i in range (1, 10):
    print(f"{a} * {i} = {i*a}")

'''
a = int(input("단수를 입력해보이소 : "))
for i in range(1, 10):
    print(f"{a:2d} * {i:2d} = {a*i:3d}" ,end="")
    if i%3 == 0 : 
        print("")