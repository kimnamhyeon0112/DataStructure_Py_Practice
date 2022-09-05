# 숫자 자리별 홀 짝 판단
for i in "7645878321":
    if(int(i) % 2 == 0):
        print(i, "짝수")
    else:
        print(i, "홀수")
print("\n")

# or
s = "7645878321"
for i in range(10):
    if int(s[i]) % 2 == 0:
        print(s[i], "짝수")
    else:
        print(s[i], "홀수")
print("\n")

# 전체 숫자 홀 짝 판단
s = "7645878321"
s = int(s)
if s % 2 == 0:
    print(s, "는 짝수")
else:
    print(s, "는 홀수")
print("\n")

# 각 자리수 합해서 출력
value = 0
for i in "7645878321":
    value += int(i)
print(value)

