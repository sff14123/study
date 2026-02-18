w, h = map(int, input().split())
n = int(input())

row_cuts = [0, h]
col_cuts = [0, w]

for _ in range(n):
    d, pos = map(int, input().split())
    if d == 0: 
        row_cuts.append(pos)
    else:
        col_cuts.append(pos)

row_cuts.sort()
col_cuts.sort()

max_h = 0
for i in range(1, len(row_cuts)):
    row = row_cuts[i] - row_cuts[i-1]
    if row > max_h:
        max_h = row

max_w = 0
for i in range(1, len(col_cuts)):
    col = col_cuts[i] - col_cuts[i-1]
    if col > max_w:
        max_w = col

print(max_h * max_w)