T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_s = 0 # 최대 점수
    d = [[1,0],[-1,0],[0,1],[0,-1]]
    for i in range(N):
        for j in range(N):
            s = arr[i][j] # 기준점
            for r in range(4):
                ni, nj = i +  d[r][0], j + d[r][1]
                while 0 <= ni < N and 0 <= nj < N:
                    s += arr[ni][nj]
                    ni += d[r][0]	# 범위 끝까지 탐색
                    nj += d[r][1]
            if s > max_s:
                max_s = s
    print(f'#{tc} { max_s}')