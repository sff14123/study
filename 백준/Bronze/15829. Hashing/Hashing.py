l = int(input())
s = input()

r = 31
m = 1234567891

total_hash = 0

for i in range(l):
    num = ord(s[i]) - ord('a') + 1

    total_hash += num * (r ** i)

print(total_hash % m)