data = ["kim_16",
        "hong_25",
        "lee_30",
        "park_15",
        "seo_20",
        "ko_24",
        "kim_22",
        "choi_30",
        "hong_15",
        "ahn_20",
        "ko_43",
        "kim_22",
        "park_26",
        "back_30",
        "ko_40",
        "kim_14"]


# print(data)
#인접한 두 값을 비교해서 앞의 값이 크면 자리바꿈
#나이를 기준으로 오름차순 정렬

# d1 = "kim_16"
# d2 = "hong_25"
#
# d1_1 = int(d1.split('_')[1])
# d2_1 = int(d2.split('_')[1])
# print(d1_1, d2_1)

for j in range(len(data)):
    for i in range(len(data)-1-j):
          a = int(data[i].split('_')[1])
          b = int(data[i+1].split('_')[1])
          if a > b:
                tmp = data[i]
                data[i] = data[i+1]
                data[i+1] = tmp
          print(data)
    print()
