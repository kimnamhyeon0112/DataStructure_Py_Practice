# 집합과 딕셔너리의 차이
# 딕셔너리
d1 = {1: "p"}
print("d1:", d1)

# 집합
a1 = [2, 5, 4, 7, 8, 2]
a2 = [2, 5, 4, 7, 8, 2]
a3 = [2, 5, 4, 7, 8, 2]
s1 = set(a1)
s2 = set(a2)
print("s1:", s1, "s2:", s2)
s3 = s1 | s2
print("s3:", s3)
s4 = s1 - s2
print(s4)
s5 = s1 & s2
print(s5)
n1 = {"hong", "park", "song", "kim"}
print(len(n1))      # 중복이 있을 땐 하나로 생각함
str1 = "hello hello world"
s6 = set(str1)
print(s6)
s7 = list(str1)
print(s7)

# Code 29
nickname_set = {'수선화', '코스모스', '들국화'}
while True:
    nickname = input("원하는 닉네임을 입력하세요: ")
    if nickname in nickname_set:
        print("이미 사용중입니다. 다시 입력해주세요.")
    else:
        sel = input("사용 가능합니다. 닉네임으로 등록하시겠습니까? (예/아니오): ")
        if sel == '예':
            print(nickname, "을(를) 닉네임으로 등록합니다")
            nickname_set = nickname_set | {nickname}
            break
        else:
            continue
print("사용 중인 닉네임:", nickname_set)

str1 = "Hey! What's up? Hello World."
char = ".'!?"

print(str1)
for c in char:
    print(c)
    str1 = str1.replace(c,"")

print(str1)

import re

str = "Hello, World, Python"
result = re.sub(",", "", str)
print(result)