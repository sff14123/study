T = 10
for tc in range(1, T+1):
    tc_n = int(input())
    arr = [list(input()) for _ in range(100)]
    length = 0
    for i in range(100):
        for j in range(100):
            left = right = j
            while left >= 0 and right < 100 and arr[i][left] == arr[i][right]:
                if right - left + 1 > length:
                    length = right - left + 1
                left -= 1
                right += 1
            left, right = j, j+1
            while left >= 0 and right < 100 and arr[i][left] == arr[i][right]:
                if right - left + 1 > length:
                    length = right - left + 1
                left -= 1
                right += 1
            Top = bottom = i
            while Top >= 0 and bottom < 100 and arr[Top][j] == arr[bottom][j]:
                if bottom - Top + 1 > length:
                    length = bottom - Top + 1
                Top -= 1
                bottom += 1
            Top, bottom = i, i+1
            while Top >= 0 and bottom < 100 and arr[Top][j] == arr[bottom][j]:
                if bottom - Top + 1 > length:
                    length = bottom - Top + 1
                Top -= 1
                bottom += 1
    print(f'#{tc_n}', length)