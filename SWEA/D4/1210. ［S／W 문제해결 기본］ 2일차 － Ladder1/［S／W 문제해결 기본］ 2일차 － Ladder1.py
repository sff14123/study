T = 10
for test_case in range(1, T + 1):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    di = [-1, 0, 0]
    dj = [0, -1, 1]
    dir = 0
    start = 0
    for j in range(100):
        if arr[99][j] == 2:
            start = j
    i = 99
    j = start
    while i > 0:
        if dir == 0:
            if 0 < j and arr[i][j-1] == 1:
                dir = 1
            elif j < 99 and arr[i][j+1] == 1:
                dir = 2
        else:
            if arr[i-1][j] == 1:
                dir = 0
        i += di[dir]
        j += dj[dir]
    print(f'#{test_case} {j}')