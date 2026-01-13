T = 10

for test_case in range(1, T + 1):
    N = int(input())
    boxes = list(map(int, input().split()))

    for i in range(N):
        max_idx = 0
        min_idx = 0
        for j in range(100):
            if boxes[j] > boxes[max_idx]:
                max_idx = j
            if boxes[j] < boxes[min_idx]:
                min_idx = j
        boxes[max_idx] -= 1
        boxes[min_idx] += 1
    max_idx = 0
    min_idx = 0
    for i in range(100):
        if boxes[i] > boxes[max_idx]:
            max_idx = i
        if boxes[i] < boxes[min_idx]:
            min_idx = i
    print(f'#{test_case} {boxes[max_idx] - boxes[min_idx]}')