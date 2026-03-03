import sys

n = int(sys.stdin.readline())
start = 666
cnt = 1
while cnt < n:
    start += 1
    if '666' in str(start):
        cnt += 1
print(start)