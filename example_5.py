# A~Z 출력
for i in range(65, 91, 1):
    print(chr(i), end='')
print()
for i in range(0,26,1):
    print(chr(ord('A')+i),end='')

# A~Z 피라미드 형태로 출력
for j in range(1, 27, 1):
    for i in range(0, 27-j, 1):
        print(" ", end='')
    for i in range(0, j, 1):
        print(chr(ord('A')+i), end=' ')
    print()

# A~Z 역삼각형 형태로 출력
for i in range(0, 27, 1):
    for j in range(i, 26, 1):
        print(chr(ord('A')+j), end='')
    print()

# A~Z 출력후 다음 줄에 하나씩 소거 하여 맨뒤로 옮김
for i in range(0, 26, 1):
    for j in range(i, 26, 1):
        print(chr(ord('A') + j), end='')
    for j in range(0, i, 1):
        print(chr(ord('A') + j), end='')
    print()

# 함수의 오버라이딩 불가
# def plus(a,b):
#     res=a+b
#     return res
def plus(a, b, c):
    res = a+b+c
    return res

def pyramid():
    for j in range(1, 27, 1):
        for i in range(0, 27 - j, 1):
            print(" ", end='')
        for i in range(0, j, 1):
            print(chr(ord('A') + i), end=' ')
        print()

def onetong():
    for i in range(0, 26, 1):
        for j in range(i, 26, 1):
            print(chr(ord('A') + j), end='')
        for j in range(0, i, 1):
            print(chr(ord('A') + j), end='')
        print()

print("[메뉴]")
print("1. 덧셈, 2. 알파벳 삼각형 출력, 3. 알파벳 원통형 출력, 0. 종료")
while True:
    menu = int(input("메뉴 선택: "))
    if menu == 1:
        res1=plus(10,30,40)
        print(res1)
    elif menu == 2:
        pyramid()
        print()
    elif menu == 3:
        onetong()
        print()
    elif menu == 0:
        print("프로그램 종료")
        exit()
    else:
        print("메뉴는 0번부터 3번까지 입니다 다시 입력하세요")
