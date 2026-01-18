T = 10
for test_case in range(1, T + 1):
    tc_num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_v = 0
    s3 = 0
    s4 = 0

    for i in range(100):

        s1 = 0
        s2 = 0

        for j in range(100):
            s1 += arr[i][j]
            s2 += arr[j][i]
        if max_v < s1:
            max_v = s1

        if max_v < s2:
            max_v = s2

        s3 += arr[i][i]
        s4 += arr[i][99 - i]

    if max_v < s3:
        max_v = s3

    if max_v < s4:
        max_v = s4

    print(f'#{tc_num} {max_v}')


