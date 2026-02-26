import sys
scr = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
total_sum = 0.0  # (학점 * 평점)의 합계
total_credit = 0.0  # 학점의 총합

for line in sys.stdin:
    sbj, credit, grade = line.split()

    # P인 과목은 계산에서 제외
    if grade == 'P':
        continue

    credit = float(credit)
    total_sum += credit * scr[grade]
    total_credit += credit

# 결과 출력
print(total_sum / total_credit)