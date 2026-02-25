import sys
numbers = list(sys.stdin.readline().split())
new_numbers = []
for number in numbers:
    new_number = number[2] + number[1] + number[0]
    new_numbers.append(int(new_number))
print(max(new_numbers))