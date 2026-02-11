A, B, C = map(int, input().split())
result = [ (A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C) * (B%C))%C]
for i in result:
    print(i)