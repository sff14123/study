n = int(input())
cnt = 0
tmp = n
new_n = -1
while new_n != n:
    if tmp < 10:
        tmp += tmp * 10
    else:
        x = (tmp // 10) + (tmp % 10)
        tmp = (tmp % 10) * 10 + (x % 10)
    cnt += 1
    new_n = tmp
print(cnt)