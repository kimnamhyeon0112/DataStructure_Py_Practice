# a,b,c=map(int,input().split())
# print(a+b+c)

# a = 50
# b = 100
# c = None
# print(a,b,c)

language, english, math, science = map(int, input().split())
avg=int((language+english+math+science)/4)
print(avg)