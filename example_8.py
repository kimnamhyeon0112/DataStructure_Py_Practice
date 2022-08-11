# 인접한 두 값을 비교해서 앞의 값이 크면 자리바꿈
data = ["hong_25", "kim_16", "lee_30", "park_15", "seo_20", "ko_24", "kim_22", "choi_30", "hong_15", "ahn_20",
        "ko_43", "kim_22", "park_26", "back_30", "ko_40", "kim_14"]
print("변경전:", data)
for j in range(len(data)):
        for i in range(len(data)-1):
                if data[i] > data[i+1]:
                        data[i], data[i+1] = data[i+1], data[i]
                        print("변경과정:", data)

print("변경후:", data)
print("sorted 사용:", sorted(data))

# 나이 기준 정렬(split 함수 사용)
# data = ["hong_25", "kim_16", "lee_30", "park_15", "seo_20", "ko_24", "kim_22", "choi_30", "hong_15", "ahn_20",
#         "ko_43", "kim_22", "park_26", "back_30", "ko_40", "kim_14"]
# print("변경전:", data)
# for j in range(len(data)):
#         for i in range(len(data)-1-j):
#                 age1 = int(data[i].split('_')[1])
#                 age2 = int(data[i+1].split('_')[1])
#                 if age1 > age2:
#                         data[i], data[i + 1] = data[i + 1], data[i]
#                 print("변경과정:", data)
# print("변경후:", data)

# 위치를 이용하여 나이 찾기
# d1 = "kim_14"
# d2 = "hong_15"
# d1_1 = int(d1[d1.find('_')+1:])
# d2_1 = int(d2[d2.find('_')+1:])
# print(d1_1, d2_1)