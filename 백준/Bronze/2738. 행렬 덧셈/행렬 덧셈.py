N, M = map(int, input().split())

arr_A = [list(map(int, input().split())) for _ in range(N)]
arr_B = [list(map(int, input().split())) for _ in range(N)]
result = []
for i in range(N):
    tmp_row = []
    for j in range(M):
        tmp_row.append(arr_A[i][j] + arr_B[i][j])
    result.append(tmp_row)
for r in result:
    print(*r)