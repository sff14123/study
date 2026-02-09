arr = []
for _ in range(9):
  N = int(input())
  arr.append(N)
sorted_arr = sorted(arr)
max_v = sorted_arr[-1]
find = 0
for i in range(9):
    if arr[i] == max_v:
        find = i + 1
        break

print(max_v)
print(find)