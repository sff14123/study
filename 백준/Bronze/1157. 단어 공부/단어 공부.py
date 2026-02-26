import sys
txt = list(sys.stdin.readline().rstrip().upper())
cnt = {}
for t in txt:
    if t in cnt:
        cnt[t] += 1
    else:
        cnt[t] = 1
rst = []
max_cnt = max(cnt.values())
for k in cnt:
    if cnt[k] == max_cnt:
        rst.append(k)
        if len(rst) > 1:
            print('?')
            break
else:
    print(*rst)