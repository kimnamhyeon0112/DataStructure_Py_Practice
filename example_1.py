# 나의 학점 계산 프로그램
# 95 = A+, 90 = A0, 85 = B+, 80 = B0, 75 = C+ 70 = C0, 65 = D+, 60 = D0, 0~59 = F
def getGrade():
    grade = ''
    if score >= 90:
        grade += 'A'
    elif score >= 80:
        grade += 'B'
    elif score >= 70:
        grade += 'C'
    elif score >= 60:
        grade += 'D'
    else:
        grade += 'F'

    if score >= 60:
        if score % 10 >= 5:
            grade += '+'
        else:
            grade += '0'
    print(grade, "학점입니다")

score = int(input("점수 입력: "))
getGrade()

# 10명의 학점 계산 프로그램(for문)
def getGrade():
    for _ in range(10):
        score = int(input("점수 입력 : "))
        grade = ''

        if score >= 0 and score <= 100:
            if score >= 90:
                grade += "A"
            elif score >= 80:
                grade += "B"
            elif score >= 70:
                grade += "C"
            elif score >= 60:
                grade += "D"
            else:
                grade += "F"
        else:
            print("올바르지 않은 점수 입니다 다시 입력 하세요")
            continue

        if score >= 60:
            if score == 100 or score % 10 >= 5:
                grade += '+'
            else:
                grade += '0'
        print(grade, "학점입니다")
getGrade()

# 10명의 학점 계산 프로그램(while문)
def getGrade():
    i = 0
    while i < 10:
        score = int(input("점수 입력 : "))
        grade = ''

        if score >= 0 and score <= 100:
            if score >= 90:
                grade += "A"
            elif score >= 80:
                grade += "B"
            elif score >= 70:
                grade += "C"
            elif score >= 60:
                grade += "D"
            else:
                grade += "F"
        else:
            print("올바르지 않은 점수 입니다 다시 입력 하세요")
            continue

        if score >= 60:
            if score == 100 or score % 10 >= 5:
                grade += '+'
            else:
                grade += '0'
        print(grade, "학점입니다")
        i += 1
getGrade()
