def enqueue(i):
    global rear
    rear = (rear + 1) % (N+1)
    cq[rear] = i
def dequeue():
    global front
    front = (front + 1) % (N+1)
    return cq[front]
T = 10
for tc in range(1, 1+T):
    tc_num = int(input())
    arr = list(map(int, input().split()))
    N = 8
    cq = [0] + arr
    front = 0
    rear = N
    i = 1
    while True:
        x = dequeue() - i
        if x <= 0:
            x = 0
            enqueue(x)
            break
        enqueue(x)
        i = (i % 5) + 1
    temp = []
    while front != rear:
        temp.append(dequeue())
    print(f'#{tc_num}', *temp)