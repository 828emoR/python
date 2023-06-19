from tkinter import *
'''
#list method

list_int=[1, 5, 7, 9, 3]
list_char=['a', 'b', 'c', 'd']
list_char.insert(2, 'z')
print(list_char)
list_char.append('z')
print(list_char)
list_char.remove('z')
print(list_char)

#list function

list_int=[1,5,7,9,3]
list_char=['a', 'b', 'c', 'b', 'c', 'c']

#리스트 정렬
print(sorted(list_int))
print(list_int)

print(list(reversed(list_int)))
print(list_int) #list 변함없음

list_int=list(reversed(list_int))
print(list_int)

#list 연습

intone=[]

for i in range (0, 10):
azaz = int(input("넣을 수를 입력하세요"))

intone.append(azaz)
print(sum(intone))
'''

#list 접근
a=[0,1,2,3,4,5,6,7,8,9]

print(a[2:3])
a[2:3]=[20,30]
print(a)

print(a[2:4])
a[2:4]=[20,30]
print(a)

a[2:5]=[20,30]
print(a)

a[2]=[20,30]
print(a)

print(a[-1],a[-2])