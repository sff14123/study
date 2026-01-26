T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    A = list(A)
    B = list(B)
    i = j = 0
    cnt = 0
    while i < len(A) and j < len(B):
        if A[i] != B[j]:
                i = i - j
                j = -1
        i += 1
        j += 1
        if j == len(B):
            cnt += 1
            j = 0
    typing = len(A) - cnt*len(B) + cnt
    print(f'#{tc}', typing)