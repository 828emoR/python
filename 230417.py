'''
t = True
f = False
print(t,f)
print(type(t))

print(10>20)

a= 10
b= 20
print(a<b)

print(True and True)
print(True and False)
print(False and True)
print(False and False)
# 문제-몸무게를 입력받아 50에서 80사이 일 경우에만 "정상"을 출력하고 나머지는 "비정상"이라고 출력하는 프로그램 만들기.


Wei = int(input(f"몸무게 입력 함 조지봐라"))
if 50<Wei<80:
    print(f"정상")
else:
    print(f"비정상")

if Wei>=50 and Wei<=80 :
    pass
else :
    print("비정상")
#해당 방법도 가능하다.

import random
for i in range (1,11):
    print(random.randrange(1, 7))


#이하의 방법도 가능하다
import random
for i in range(1, 11):
rand_val = random.randrange(1,7,1)
print(rand_val)


score = int(input("입력>"))
print(score)
score = score/10
match score:
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
        print("unknown")

import random
c1 = c2 = c3 = c4 = c5 = c6 = 0
for i in range (1, 101):
    rand_val = random.randrange(1, 7)
    match rand_val:
        case 1:
            c1 = c1 + 1
        case 2:
            c2 = c2 + 1
        case 3:
            c3 = c3 + 1
        case 4:
            c4 = c4 + 1
        case 5:
            c5 = c5 + 1
        case 6:
            c6 = c6 + 1
    p
    '''
'''
//##List Method##//
list_int=[1,5,7,9,3]


import random
c = []
for i in range (1,8):
    c.append(0)
print(c)

for i in range(1, 101):
    rand_val = random.randrange(1,7)
    c[rand_val] = c[rand_val] + 1
print(f"{i}의 갯수는 c+{i}개 입니다.")

'''
 #동전을 던져 앞면 뒷면을 맞추는 문제
 #입력: 1. 앞면 2. 뒷면
 #출력: 사용자 : 앞면 선택
    #   컴퓨터: 앞면, 뒷면
    #   맞음 , 틀림 출력하는것.
import random
R = random.randrange(0, 1 +1)
# print(R)
i = int(input("앞면 (0), 뒷면 (1)\n > "))

if i == R:
    print(f"값은{R}, 입력값은 {i} 맞췄습니다.")
else:
    print(f"값은{R}, 입력값은{i} 틀리셨습니다.")
    if i != R:
        print("0과 1중에 선택해주세요")
