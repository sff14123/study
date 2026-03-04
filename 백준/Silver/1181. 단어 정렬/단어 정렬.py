import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    txt = sys.stdin.readline().rstrip()
    if not txt in arr:
        arr.append(txt)
arr.sort()
arr.sort(key=len)
for i in arr:
    print(i)