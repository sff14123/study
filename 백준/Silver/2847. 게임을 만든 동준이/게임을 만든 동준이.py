# 처음부터 탐색 or 끝에서 내려오면서
# 다시 처음부터 검사하게 하는 옵션은? - 마지막을 기준으로 탐색하며 내려오기

N = int(input())
scores = [int(input()) for _ in range(N)]
cnt = 0
for i in range(N-1, 0, -1):
        if scores[i] <= scores[i - 1]:
            target = scores[i] - 1
            decrease = scores[i - 1] - target
            cnt += decrease
            scores[i-1] = target

print(cnt)