# 대문자, 소문자 변경
# s1 = "Literature, history, philosophy and youth are alive."
#
# print("s1[4]:", s1[4])
# # s1[4] = 'R'
# # s1.append('!!')
# s2 = s1[4:10]
# s3 = s1.upper()
# s4 = s1.lower()
# print("s1:", s1)
# print("s2:", s2)
# print("s3:", s3)
# print("s4:", s4)

# s1 = "Literature, history, philosophy and youth are alive."
# res = ''
# a = 'i'

# for i in s1:
#     if 'a' <= i <= 'z':
#         pass
#     elif 'A' <= i <= 'Z':
#         res += i

# res1 = ''
# for i in range(len(s1)):
#     if 'a' <= s1[i] <= 'z':
#         pass
#     elif 'A' <= s1[i] <= 'Z':
#         res += s1[i]

# res = ''
# for i in s1:
#     if 'a' <= i <= 'z':
#         res += chr(ord(i) - 32)
#     elif 'A' <= i <= 'Z':
#         res += i
#
# res1 = ''
# for i in range(len(s1)):
#     if 'a' <= s1[i] <= 'z':
#         res1 += chr(ord(s1[i]) - 32)
#     elif 'A' <= s1[i] <= 'Z':
#         res1 += s1[i]
# print(res)
# print(res1)
#
# print(s1.count('Literature'))
# print(s1.find('a'))
# print(s1.index('a'))
#
# r1 = s1.find('z')
# if r1 != -1:
#     print(r1)
# else:
#     print("해당문자 없음")
#
# s1 = "Literature, history, philosophy and youth are alive."
# print(s1.startswith('Li'))
# print(s1.endswith('are'))
# print(s1.split())   # 띄어쓰기단위로 단어분류
#
# s2 = "Literature,-history,-philosophy-and-youth-are-alive."
# print(s2.split('-'))
# print(s2.strip())
#
# s3 = "@Liter ature@"
# print(s3.split('@'))
#
# s4 = '123'
# print(s4.isdigit())
#
# a = ''
# s5 = ['Literature', 'history', 'philosophy', 'and', 'youth', 'are', 'alive.']
# print(' '.join(s5))

# data = ["hong_25",
#         "kim_16",
#         "lee_30",
#         "park_15",
#         "seo_20",
#         "ko_24",
#         "kim_22",
#         "choi_30",
#         "hong_15",
#         "ahn_20",
#         "ko_43",
#         "kim_22",
#         "park_26",
#         "back_30",
#         "ko_40",
#         "kim_14"]

# namelist = []
# agelist = []
#
# t = "hong_25"
# t1 = t.split('_')
# namelist.append(t1[0])
# agelist.append(t1[1])
#
# tmp = t.split
#
# for i in data:
#     if data[i].isalpha == True:
#         namelist = data[i]
#     elif data[i].isdigit == True:
#         agelist = data[i]
# print(namelist)
# print(agelist)

# 2차원 리스트
# stu1 = [5, 4, 6, 7]
# stu2 = [8, 4, 3, 7]
# stu3 = [4, 4, 6, 5]
# stu4 = [7, 4, 9, 7]
# stuAll = [stu1, stu2, stu3, stu4]
# print(stuAll)
# print(stuAll[2])
# print(stuAll[2][1])
# stuAll[2][1] = 10
# print(stuAll[2][1])
#
# for i in stuAll:
#         print(i, end=' ')
# print()
#
# for a in stuAll:
#         for i in a:
#                 print(i, end=' ')
#         print()

# 2차원 리스트 값 중에서 2의 배수를 모두 0으로 바꾸기
# stu1 = [5, 4, 6, 7, 9]
# stu2 = [8, 4, 3, 7, 4]
# stu3 = [4, 4, 6, 5, 8]
# stu4 = [7, 4, 9, 7, 5]
# stuAll = [stu1, stu2, stu3, stu4]
#
# print("원본:", stuAll)
# print("수정본:")
# for a in stuAll:
#         for i in a:
#                 if i % 2 == 0:
#                         i = 0
#                 print(i, end=' ')
#         print()

# 원본을 영행렬로 바꾸기
# stuAll = [[5, 4, 6, 7], [8, 4, 3, 7], [4, 4, 6, 5], [7, 4, 9, 7]]
#
# for a in stuAll:
#         for i in a:
#                 i = 0
#                 print(i, end=' ')
#         print()
#
# # or
# for i in range(0,4,1):
#         res = []
#         for j in range(4):
#                 res.append(0)
#         print(res)

# Ch7 code 19
# class1 = [
#         [88, 75, 96, 74, 82],
#         [72, 82, 63, 88, 76],
#         [92, 84, 82, 96, 76]
# ]
#
# sum = 0; i = 0; numSubj = 0
# for stu in class1:
#         sum = 0
#         for subj in stu:
#                 sum += subj
#         avg = sum / len(stu)
#         print("%d번 학생 : 총점=%d, 평균=%6.2f" % (i, sum, avg))
#         i = i + 1
#         numSubj += len(stu)
#         classSum = sum + sum
# avgClass = sum / (numSubj)
# print("전체 평균 = %6.2f" % (avgClass))
# print()
#
# print(class1)
# print()
# for stu in class1:
#         sum = 0
#         for subj in stu:
#                 sum+=subj
#         stu.append(sum)
# print(class1)

# 행 열 반대로 print
# stuAll = [[5, 4, 6, 7], [8, 4, 3, 7], [4, 4, 6, 5], [7, 4, 9, 7]]
#
# print("원본:")
# for a in stuAll:
#         for i in a:
#                 print(i, end=' ')
#         print()
# print()
#
# print("수정본:")
# for i in range(len(stuAll)):
#         for j in range(len(stuAll[i])):
#                 print(stuAll[j][i], end=' ')
#         print()

# 2, 4행 순서 변경
# stuAll = [[5, 4, 6, 7], [8, 4, 3, 7], [4, 4, 6, 5], [7, 4, 9, 7]]
# print("원본:")
# for a in stuAll:
#         for i in a:
#                 print(i, end=' ')
#         print()
# print()
#
# print("수정본:")
# for i in range(len(stuAll)):
#         if i % 2 == 0:
#                 for j in range(len(stuAll[i])):
#                         print(stuAll[i][j], end=' ')
#         else:
#                 for j in range(len(stuAll[i])-1, -1, -1):
#                         print(stuAll[i][j], end=' ')
#         print()

# 1열 3열 순서 변경
# stuAll = [[5, 4, 6, 7],
#           [8, 4, 3, 7],
#           [4, 4, 6, 5],
#           [7, 4, 9, 7]]
# print("원본:")
# for a in stuAll:
#         for i in a:
#                 print(i, end=' ')
#         print()
# print()
#
# print("수정본:")
# for i in range(len(stuAll)):
#         if i % 2 == 0:
#                 for j in range(len(stuAll[i])-1,-1,-1):
#                         print(stuAll[i][j], end=' ')
#         else:
#                 for j in range(len(stuAll[i])):
#                         print(stuAll[i][j], end=' ')
#         print()
#
# print("수정본2:")
# for i in range(len(stuAll[0])):
#         for j in range(len(stuAll)):
#                 print(stuAll[j][i], end=' ')
#         print()
# print()
