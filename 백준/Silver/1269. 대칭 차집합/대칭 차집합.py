a, b = map(int, input().split())
arr_a = {int(x) for x in input().split()}
arr_b = {int(x) for x in input().split()}
rst = len(arr_a ^ arr_b)
print(rst)