sum_99 = 0
sum_100 = 0
s = 0

for _ in range(10):
   mush = int(input())
   s += mush
   if s < 100:
       sum_99 = s
   else:
        sum_100 = s
        break

if sum_100 == 0:
    print(sum_99)
else:
    A = 100 - sum_99
    B = sum_100 - 100
    if A >= B:
        print(sum_100)
    else:
        print(sum_99)