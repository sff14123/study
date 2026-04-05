t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    y = x = 0
    if n % h == 0:
        y = str(h)
        x = n // h
    else:
        y = str(n % h)
        x = n // h + 1
    if x < 10:
        x = '0' + str(x)
    else:
        x = str(x)
    print(y + x)