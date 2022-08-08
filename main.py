# 변수 선언
print("Hello")
name_1="Kim"
age_1=23
phone_1="01058119122"
type_1='A'
type_2="B it's B"
num=3.14

# 사칙연산
a=127
b=300
c="345"
d="867"
# 127+300=427
# 127+300=127300

res1= a+b
print(res1)

str1="Hello"
print(str1)

res2=str(a) + str(b)
print(res2)

res3=c+d
print(res3,c,d)

res4=int(c)+int(d)
print(res4)

# 조건문
if a == 127:
    print("True")
    print("True1")
else:
    print("False")

# 타입 확인
f=3.14
print(type(a))
print(type(f))
print(type(d))

f="3.14"
f1=1.592
res5=float(f)+f1
print(res5)

res6=f+str(f1)
print(res6)

a=128
res1=128/3
res2=128%3
res3=128//3
print(res1,res2,res3)

a=128
if(a%2==1):
    print("홀수")
else:
    print("짝수")

#score=int(input("점수 입력: "))
#score+=10
#print("당신의 점수는",score+10,"입니다")

# 반복문
# range(start, stop+1, step)
# ex) range(0, 10, 1) -> 0~9 출력
# ex) rnage(0, 21, 2) -> 0~20 짝수 출력
# ex) rnage(1, 31, 3) -> 1~31 +3씩 출력
# ex) range(10) == range(0, 10, 1)
# ex) range(1, 10) == range(1, 10, 1)
for i in range(0, 10 ,1):
    print("Hello")
print('-'*20)

for i in range(0,20,1):
    print(i, "Hello")

for i in "7645878321":
    print(i)

# 논리 연산자 조건 처리
# A조건   B조건    A 그리고(and) B     A 또는(or) B
#   T      T            T               T
#   T      F            F               T
#   F      T            F               T
#   F      F            F               F
a = 10; b = 20
if a > b:
    print("T")

if a < b:
    print("T")

if a > b and a % 2 == 0:
    print("T and T")

# while문
# while 조건:
#       명령문
s = " 7645878321"
res = len(s)
value1 = 0
i = 0
while i < len(s):
    print(i)
    value1 += int(s[i])
    i += 1
print(value1)

value2 = 0
while True:
    v = int(input("값: "))

    if v < 0:
        break
        value2 += v