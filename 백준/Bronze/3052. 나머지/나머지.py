import sys

arr = []
for line in sys.stdin:
    a = int(line) % 42
    if not a in arr:
        arr.append(a)
print(len(arr))