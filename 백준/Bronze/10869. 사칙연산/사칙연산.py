A, B = map(int, input().split())
result = [A+B, A-B, A*B, A//B, A%B]
for i in result:
    print(i)