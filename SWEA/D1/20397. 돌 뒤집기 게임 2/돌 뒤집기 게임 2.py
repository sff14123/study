T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for m in range(M):
        i, j = map(int, input().split())
        left = right = i-1 # i번째 돌과 같은 위치로 좌우를 설정
        for k in range(j):
            left -= 1
            right += 1
            if left < 0 or right > N - 1:
                break
            if arr[left] == arr[right]:
                arr[left] = arr[right] = 1 - arr[left]
    print(f'#{tc}', *arr)