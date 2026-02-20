dwarfs = [int(input()) for _ in range(9)]
found = False

for i in range(9):
    for j in range(i+1, 9):
        if sum(dwarfs) - (dwarfs[i] + dwarfs[j]) == 100:
            dwarfs1, dwarfs2 = dwarfs[i], dwarfs[j]
            dwarfs.remove(dwarfs1)
            dwarfs.remove(dwarfs2)
            found = True
            break
    if found:
        break

dwarfs.sort()
for d in dwarfs:
    print(d)