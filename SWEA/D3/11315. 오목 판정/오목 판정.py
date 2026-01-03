T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    d = [[1, 0], [0, 1], [1, 1], [1, -1]]
    max_cnt = 0
    for i in range(N):
        for j in range(N):
            for dir in range(4):
                cnt = 0
                for k in range(N):
                    ni, nj = i+d[dir][0]*k, j+d[dir][1]*k
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                        cnt += 1
                        if max_cnt < cnt:
                            max_cnt = cnt
                    else:
                        cnt = 0
    if max_cnt > 4:
        result = 'YES'
    else:
        result = 'NO'
    print(f'#{tc} {result}')