A, B = list(map(str, input().split()))
N = len(A)
M = len(B)
arr = [list('.' * N) for _ in range(M)]
for i in range(N):
    for j in range(M):
        if A[i] == B[j]:
            cross_i = i
            cross_j = j
            break
    else:
        continue
    break

for row in range(M):
    if row == cross_j:
        arr[row] = A  
    else:
        arr[row][cross_i] = B[row]
for line in arr:
    print(''.join(line))