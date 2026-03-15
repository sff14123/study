count = 0
result = -1

def merge_sort(A, p, r, K):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q, K)  
        merge_sort(A, q + 1, r, K)  
        merge(A, p, q, r, K)  

def merge(A, p, q, r, K):
    global count, result
    i, j = p, q + 1
    tmp = []

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    while i <= q:
        tmp.append(A[i])
        i += 1
    while j <= r:
        tmp.append(A[j])
        j += 1

    for t in range(len(tmp)):
        A[p + t] = tmp[t]
        count += 1
        if count == K:
            result = A[p + t]

N, K = map(int, input().split())
A = list(map(int, input().split()))
merge_sort(A, 0, len(A) - 1, K)
print(result)