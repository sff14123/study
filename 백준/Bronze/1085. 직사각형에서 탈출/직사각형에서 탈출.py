x, y, w, h = map(int, input().split())
min_x = min((x-0), (w-x))
mix_y = min((y-0), (h-y))
print(min(min_x, mix_y))