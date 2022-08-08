# Chap 04 page 20 code 9
num1= int(input("정수 입력: "))
num2= int(input("정수 입력: "))
if num2 == 0:
    print("ERROR: divide by zero\n")
else:
    result = num1 / num2
    print("num1/num2 =", result)
    print("프로그램 종료")

# Chap 04 page 29 code 15
# 윤년: 4 또는 400의 배수면서 100의 배수가 아닌 연도
year = int(input("연도 입력: "))
if year % 4 != 0:
    print("%d년은 윤년이 아닙니다!" % year)
elif year % 100 == 0 and year%400 == 0:
    print("%d년은 윤년입니다!" % year)
elif year % 100 == 0 and year%400 != 0:
    print("%d년은 윤년이 아닙니다!" % year)
else:
    print("%d년은 윤년입니다!" % year)

# Chap 05 page 12 code 12
print("-1을 입력할 때까지 입력되는 정수의 합 구하기")
num = int(input("정수 입력 : "))
sum = 0
while num != -1:
    sum = sum + num
    num = int(input("정수 입력 : "))
    print("입력된 정수의 합 : ", sum)

# Chap 05 page 33 code 17
n = int(input("양의 정수: "))
flag = 0
for i in range(2, n) :
    if n % i == 0:
        flag = 1
if flag == 0:
    print("%d은 소수임" %(n))
else:
    print("%d은 소수가 아님" %(n))