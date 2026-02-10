N = 19
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

directions = [(0,1), (1,0), (1,1), (-1,1)]  # 오른쪽, 아래, 대각선 ↘, 대각선 ↗

winner = 0
win_pos = ()

for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            continue
        color = arr[i][j]

        for dx, dy in directions:
            cnt = 1
            x, y = i, j

            # 뒤쪽 돌 확인 (6목 방지)
            prev_x, prev_y = i - dx, j - dy
            if 0 <= prev_x < N and 0 <= prev_y < N and arr[prev_x][prev_y] == color:
                continue

            # 앞으로 4개 돌 확인
            for k in range(1,5):
                ni, nj = i + dx*k, j + dy*k
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == color:
                    cnt += 1
                else:
                    break

            # 5목 확인
            if cnt == 5:
                # 6목 방지: 6번째 돌이 있는지 확인
                ni, nj = i + dx*5, j + dy*5
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == color:
                    continue

                winner = color
                win_pos = (i+1, j+1)  # 1-based 좌표
                break
        if winner != 0:
            break
    if winner != 0:
        break

print(winner)
if winner != 0:
    print(win_pos[0], win_pos[1])
