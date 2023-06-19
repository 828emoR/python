#dictionary - 접근

dic_stud={'학과':'IT','학번':21001, '학년':2, '이름':'아이티'}
print(dic_stud)
dic_stud['핸폰']='010-0000-0000'
print(dic_stud)
print(dic_stud['학과'])
dic_stud['학과']='기계'
print(dic_stud)
del(dic_stud['학과'])
print(dic_stud) 
dic_stud={'학과':'IT','학번':21001, '학년':2, '이름':'아이티','학년':1}
print(dic_stud)
#.get()
print(dic_stud'학교')
print(dic_stud'이름')
print(dic_stud.get('이름'))
print(dic_stud('주소'))


print(dic_stud.keys)
print(list(dic_stud.keys))
for i in dic_stud.keys():
    print(i)
print(dic_stud.values())
for i in dic_stud.values():
    print (i)
    print(dic_stud.items())
    print('이름' in dic_stud)
    print('주소' in dic_stud)


print(dic_stud)
for i in dic_stud