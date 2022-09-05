# Page 31 Code 20
# class1 = [
#             [88, 75, 96, 74, 82],
#             [72, 82, 63, 88, 76],
#             [92, 84, 82, 96, 76]
#         ]
# totsum = 0
# for i in range(len(class1)):
#     sum = 0
#     for j in range(len(class1[0])):
#         sum += class1[i][j]
#     avg = sum/len(class1[0])
#     print("%d번 학생: 총점=%d, 평균=%.2f"% (i, sum, avg))
#     totsum += sum
# totavg = totsum/(len(class1)*len(class1[0]))
# print("전체 평균 = ", totavg)

# Page 32 Code 21
# flowers = ['장미', '튤립', '수선화', '카네이션', '국화']
# buy_flower = input("구매할 꽃을 알려주세요:")
# if buy_flower in flowers:
#     print("감사합니다. 바로 준비하겠습니다.\n 조금만 기다려주세요.")
# else:
#     print("죄송합니다. 요청하신 꽃은 없습니다.\n 빠른 시일 내에 준비하겠습니다.")

# Page 59 Code 35
infoHobby = { '바둑': 5, '독서': 5, '영화감상': 5}
print("통계 조사 전", infoHobby)
for i in range(5):
    print("학생들의 여가 활동에 대한 통계 조사 중입니다")
    survey=input("학생의 여가활동은 무엇입니까?: ")
    if survey in infoHobby.keys():
        infoHobby[survey]+=1
    else:
        infoHobby[survey] = 1
print("5명의 통게 조사 후:", infoHobby)