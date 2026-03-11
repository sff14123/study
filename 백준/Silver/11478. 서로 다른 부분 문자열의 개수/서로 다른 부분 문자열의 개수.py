s = input()
rst = set()
for i in range(len(s)):
    for j in range(i, len(s)):
        rst.add(s[i:j+1])
print(len(rst))