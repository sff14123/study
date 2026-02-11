arr = list(input())
cnt = 0

for i in range(len(arr)):
    if arr[i] == 'Y':
        cnt += 1
        arr[i] = 'N'
        if i < len(arr):
            for j in range(i+1,len(arr)):
                if (j+1) % (i+1) == 0:
                    if arr[j] == 'Y':
                        arr[j] = 'N'
                    else:
                        arr[j] = 'Y'
if 'Y' in arr:
    cnt = -1
print(cnt)