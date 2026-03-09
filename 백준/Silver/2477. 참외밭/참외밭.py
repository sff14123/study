k = int(input())
edges = []
for _ in range(6):
    direction, length = map(int, input().split())
    edges.append(length)
max_w = 0
max_h = 0
w_idx = 0
h_idx = 0

for i in range(6):
    if i % 2 == 0:
        if max_w < edges[i]:
            max_w = edges[i]
            w_idx = i
    else:
        if max_h < edges[i]:
            max_h = edges[i]
            h_idx = i
small_w = abs(edges[(h_idx + 5) % 6] - edges[(h_idx + 1) % 6])
small_h = abs(edges[(w_idx + 5) % 6] - edges[(w_idx + 1) % 6])

total_area = (max_w * max_h) - (small_w * small_h)
print(total_area * k)