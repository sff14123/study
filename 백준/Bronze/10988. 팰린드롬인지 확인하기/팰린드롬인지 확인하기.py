import sys
txt = sys.stdin.readline().rstrip()
for t in txt:
    left = 0
    right = len(txt)-1
    while left < right:
        if txt[left] == txt[right]:
            left += 1
            right -= 1
        else:
            print(0)
            break
    else:
        print(1)
        break
    break