n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
rank = []
for i in range(n-1):
    if arr[i][1] < arr[i+1][1]: # 금메달 비교
        arr[i], arr[i+1] = arr[i+1], arr[i]
    elif arr[i][1] == arr[i+1][1]:
        if arr[i][2] < arr[i+1][2]: # 은메달 비교
            arr[i], arr[i+1] = arr[i+1], arr[i]
        elif arr[i][2] == arr[i+1][2]:
            if arr[i][3] < arr[i+1][3]: # 동메달 비교
                arr[i], arr[i+1] = arr[i+1], arr[i]
# 동일 점수 공동 등수로 만들기
for i in range(n):
    cnt = 0
    if arr[i][0] == k:
        cnt += 1
    if cnt == 1:
        print(i+1)
        break
    else:
        print(i+2-cnt)
        break