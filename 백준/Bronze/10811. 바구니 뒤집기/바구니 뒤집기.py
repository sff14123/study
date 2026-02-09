N, M = map(int,input().split())
arr = [x for x in range(1, N+1)]
N -= 1
for m in range(M):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    while j > i:
        arr[i], arr[j] = arr[j], arr[i]
        j -= 1
        i += 1
print(*arr)