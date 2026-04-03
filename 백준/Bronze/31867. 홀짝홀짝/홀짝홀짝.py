n = int(input())
k = str(input())
x = 0
y = 0
for t in k:
    t = int(t)
    if t % 2 == 0:
        x += 1
    else:
        y += 1
if x > y:
    print(0)
elif x < y:
    print(1)
else:
    print(-1)