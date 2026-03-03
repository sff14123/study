import sys

n = int(sys.stdin.readline())
cnt = -1
found = False
for i in range(n//3+1):
    for j in range(n//5+1):
        if not i*3 + j*5 > n:
            if i*3+j*5 == n:
                cnt = i+j
                found = True
                break
    if found:
        break

print(cnt)