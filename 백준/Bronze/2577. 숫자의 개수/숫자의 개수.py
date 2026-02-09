A = int(input())
B = int(input())
C = int(input())
total = A*B*C
arr = list(str(total))
for i in range(10):
    print(arr.count(str(i)))