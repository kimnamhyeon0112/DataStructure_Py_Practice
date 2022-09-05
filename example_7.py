# Page 19 code 8
score = []
student = int(input("학생 수: "))
for i in range(0, student):
    jumsu = int(input("시험 성적: "))
    score.append(jumsu)
print("score=", score)

# Page 20 code 9
nickname=[]
for i in range(3):
    enter_name=input("닉네임 입력: ")
    nickname.append(enter_name)
print(nickname,"리스트 크기: ",len(nickname))
second_enter=input("닉네임 2번째 추가 입력: ")
nickname.insert(2,second_enter)
print("두 번째 추가결과: ",nickname, "리스트 크기: ",len(nickname))
nickname.sort()
print(nickname)
nickname.reverse()
print(nickname)

# Page 24 code 12
score = [88, 54, 84, 75, 92]
sum = 0
n = len(score)
for i in range(0, n):
    sum += score[i]
avg = sum / n
print("리스트 score 평균 : %6.2f" % avg)

# Page 53 code 30
user = {'name': "키메라", 'nickname': "수선화", 'coin': 5000, 'level': "중" }
car = {"차량번호": '한국 가 1234', "차종": '제니시스 G90', "색상": '검정', "배기량": 3800}
infoHobby = {'바둑': 10, '독서': 8, '영화감상': 7}
print("user= ", user)
print("car= ", car)
print("infoHobby= ", infoHobby)
print(user['name'], "님은", car['색상'], car['차종'], "을 운전하며 보유코인은 ", user['coin'], "입니다")

# Page 54 code 31
hobby = { '바둑': 10 , '독서' : 8, '영화감상': 7 }
print(hobby)
hobby['영화감상'] = "100명"
print(hobby)
hobby['등산'] = 20
hobby['여행'] = 30
print(hobby)
del(hobby['바둑'])
print(hobby)