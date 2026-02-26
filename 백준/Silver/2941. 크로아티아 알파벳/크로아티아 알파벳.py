import sys
txt = sys.stdin.readline().rstrip()
alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for a in alpha:
    txt = txt.replace(a, "*")
print(len(txt))