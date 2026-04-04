t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    rst = [a % 10]
    for i in range(2, b+1):
        x = a ** i % 10
        if x in rst:
            break
        rst.append(x)
    end = b % len(rst) - 1
    if rst[end] != 0:
        print(rst[end])
    else:
        print(10)