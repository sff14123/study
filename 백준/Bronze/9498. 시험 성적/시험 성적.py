score = int(input())
# 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F
if score > 89:
    print('A')
elif score > 79:
    print('B')
elif score > 69:
    print('C')
elif score > 59:
    print('D')
else:
    print('F')