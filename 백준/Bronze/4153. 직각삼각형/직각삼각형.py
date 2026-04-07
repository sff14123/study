import sys

for line in sys.stdin:
    nums = sorted(map(int, line.split()))
    
    a, b, c = nums
    
    if a == b == c == 0:
        break
    
    if a**2 + b**2 == c**2:
        print('right')
    else:
        print('wrong')