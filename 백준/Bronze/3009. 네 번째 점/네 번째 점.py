cnt_x = {}
cnt_y = {}
for _ in range(3):
    x, y = map(int, input().split())
    if x not in cnt_x:
        cnt_x[x] = 1
    else:
        cnt_x[x] += 1
    if y not in cnt_y:
        cnt_y[y] = 1
    else:
        cnt_y[y] += 1
solve_x = -1
solve_y = -1

for k, v in cnt_x.items():
    if v == min(cnt_x.values()):
        solve_x = k
for k, v in cnt_y.items():
    if v == min(cnt_y.values()):
        solve_y = k
print(solve_x, solve_y)