# 상수의 진수 변환
num = 10
print(bin(num), oct(num), hex(num))
print("----------------------")

# 알파벳
al = 'A'
n = 3
res = ord(al)+n       # ord = ascii 코드로 변환
print(chr(res))     # chr = 숫자를 문자로 출력
print("----------------------")

# 함수 선언(매개변수 순서 변경)
def showInfo(name, phone, age):
    print("이름: ", name)
    print("전화: ", phone)
    print("나이: ", age)

showInfo("홍길동", "서울", 25)
print()
showInfo(phone="서울", name="홍길동", age=25)

# 리스트
alist = [10, 30, 50, 7, 9]
for i in range(1, 100, 1):
    pass
for i in "Hello world":
    pass

s1 = 0
for c in alist:
    s1 += c

s2 = 0
for c in [10, 30, 50, 7, 9]:
    s2 += c

s3 = 0
for c in range(len(alist)):
    s3 += alist[c]

# 리스트 수정, 추가 및 삭제
alist = [5, 4, 67, 5, 2, 3, 6, 5, 7, 8, 9, 2]
print("길이:", len(alist))
print(alist[0])

# alist[0] = 50   # 수정
print("수정:", alist)

# del(alist[0])   # 삭제
print("길이:", len(alist), "삭제:", alist)
del(alist[::2])
print("삭제:", alist)     # 짝수번 째 원소 모두 삭제

alist.append(60)    # 무조건 맨 뒤에 추가
print("추가:", alist)

alist.insert(1, 100)  # 원하는 위치에 값 추가
print("추가:", alist)

alist[3] = [5, 10]
print("추가:", alist)
alist[3:4] = [15, 110]
print("추가:", alist)
alist[3:7] = [125, 1910]
print("추가:", alist)

print("검색:", alist[1:4], ",", alist[:6], ",", alist[:5])    # 검색

alist = [5, 4, 67, 5, 2]
blist = [5, 2, 3, 6, 5, 7, 8, 9, 2]
clist = alist + blist
dlist = blist*3
print("clist:", clist)
print("dlist:", dlist)

print("2의 갯수:", dlist.count(2))     # list 관련 함수

# 리스트 함수 만들기
def mycount(vlist, data):
    cnt = 0
    for c in vlist:
        if c == data:
            cnt += 1

    return cnt
res1 = mycount(dlist, 2)
print("2의 갯수:", res1)

dlist.pop(0)
print("0번째 인덱스 삭제:", dlist)

flist = [5, 42, 3, 6, 15, 7, 8, 9, 2, 25, 2, 3, 6, 5]      # 리스트 정렬
flist.sort()
print("flist 정렬:", flist)
print("flist 정렬:", sorted(flist))

flist = [5, 42, 3, 6, 15, 7, 8, 9, 2, 25, 2, 3, 6, 5]
res = flist.index(6)
print(res)

alist = list()       # 빈 리스트 생성법 2
print(alist)

# 1~9를 초기화 한 리스트에 순차적으로 추가
blist = []      # or blist = list()
for i in range(1, 10, 1):
    blist.append(i)
print("blist:", blist)

clist = [i for i in range(1, 10, 1)]
print("clist:", clist)

dlist = [n*n for n in range(1, 21)]
print("dlist:", dlist)

elist = [i for i in range(1, 21) if i % 2 == 0]
print("elist:", elist)

flist = [i if i % 2 == 0 else i * 10 for i in range(1, 21)]
print("flist:", flist)

# 튜플
tu1 = (1, 2, 5)
print(tu1)

print(tu1[1])
# tu1[1]=20
print(tu1)

def mathfunc(a, b):
    res = a + b
    return res

def mathfunc2(a, b):
    res = a - b
    return res

def mathAll(a, b):
    r1 = a + b
    r2 = a - b
    r3 = a * b
    r4 = a / b
    return r1, r2, r3, r4

res1 = mathfunc(10, 20)
print(res1)

res1 = mathfunc2(10, 20)
print(res1)

res5 = mathAll(10, 20)
for i in res5:
    print(i)
print(res5)

# 값 교환(일반적인 형태)
a = 20
b = 60
print(a, b)
temp = a
a = b
b = temp
print(a, b)

# 값 교환(파이썬 버전)
a, b = b, a
print(a, b)

d1 = {}
print(d1)

d2 = {"s1100": "hong", "s2290": "choi", "s2130": "hong"}
print(d2)

d2['s4350'] = "lee"
print(d2)

d2['s2290'] = "choi"
print(d2)

del(d2['s2290'])
print(d2)

if "s2290" in d2.keys():
    d2["s2290"] = "choi"
print(d2)

if "s2291" in d2.keys():
    d2["s2291"] = "kim"
print(d2)

res1 = d2.keys()
print(res1)

res2 = d2.items()
print(res2)

# 학번: 이름
for k in d2.keys():
    print(k, ":", d2[k])

#
d2 = {}
for k, v in d2.items():
    print(k, ":", v)
for value in d2.items():
    print(value)
