n, m = map(int, input().split())
arr = {input() for _ in range(n)}
arr2 = [input() for _ in range(m)]
cnt = 0
for i in arr2:
    if i in arr:
        cnt += 1
print(cnt)