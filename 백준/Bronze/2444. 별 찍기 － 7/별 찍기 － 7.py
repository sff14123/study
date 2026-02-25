import sys
n = int(sys.stdin.readline())
m = 2*n - 1
for i in range(1, n+1):
    star_n = i*2 - 1
    print(' ' * ((m - star_n) // 2) + '*' * star_n)
for i in range(n-1, 0, -1):
    star_n = i * 2 - 1
    print(' ' * ((m - star_n) // 2) + '*' * star_n)