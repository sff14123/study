C = int(input())
for _ in range(C):
    temp = list(map(int, input().split()))
    N = temp[0]
    arr = temp[1:]
    s = 0
    cnt = 0
    for i in arr:
        s += i
    average = s / N
    for i in arr:
        if i > average:
            cnt += 1
    result = cnt / N * 100
    print("{:.3f}%".format(result))