import sys
n = sys.stdin.readline().rstrip()
ans = 0
for i in range(1, int(n)+1):
    tmp = 0
    for j in str(i):
        tmp += int(j)
    if i + tmp == int(n):
        ans = i
        break
print(ans)