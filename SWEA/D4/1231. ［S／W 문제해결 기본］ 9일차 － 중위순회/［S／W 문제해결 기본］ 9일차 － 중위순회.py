for tc in range(1, 11):
    N = int(input())
    p = [0] * (N + 1)
    l = [0] * (N + 1)
    r = [0] * (N + 1)
    for _ in range(N):
        arr = list(input().split())
        idx = int(arr[0])
        p[idx] = arr[1]
        l[idx] = int(arr[2]) if len(arr) > 2 else 0
        r[idx] = int(arr[3]) if len(arr) > 3 else 0

    def inorder(n):
        if n == 0:
            return ''
        return inorder(l[n])+p[n]+inorder(r[n])
    print(f'#{tc} {inorder(1)}')