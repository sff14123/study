a, b = map(int, input().split())
t = int(input())
a = a * 60
b = a + b + t
h = b//60
if h >= 24:
    h -= 24
m = b%60
print(h, m)