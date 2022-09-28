'''
A 학교에서는 단체 티셔츠를 주문하기 위해 학생별로 원하는 티셔츠 사이즈를
조사했습니다.
선택할 수 있는 티셔츠 사이즈는 작은 순서대로
"XS", "S", "M", "L", "XL", "XXL" 총 6종류가 있습니다.
학생별로 원하는 티셔츠 사이즈를 조사한 결과가 들어있는
리스트 shirt_size가 매개변수로 주어질 때,
사이즈별로 티셔츠가 몇 벌씩 필요한지 가장 작은 사이즈부터
순서대로 리스트에 담아 return 하도록 함수를 완성해주세요.
'''



def myfunc(shirt):
    order = [0,0,0,0,0,0]

    for s in shirt:
        if s == 'XS':
            order[0] += 1
        elif s == 'S':
            order[1] += 1
        elif s == 'M':
            order[2] += 1
        elif s == 'L':
            order[3] += 1
        elif s == 'XL':
            order[4] += 1
        elif s == 'XXL':
            order[5] += 1

    return order

data = ["XS", "S", "XS", "S", "S", "XS","L","S", "XS","L", "S", "XS","L", "XS", "S", "L","XL", "S","XS", "S", "XS","S", "S", "XS","L"]
result = myfunc(data)
print(result)