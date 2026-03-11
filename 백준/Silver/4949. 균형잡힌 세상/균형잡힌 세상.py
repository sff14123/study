def solve(line):
    stack = []
    for char in line:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                return False
            stack.pop()
    return not stack

while True:
    line = input()
    if line == '.':
        break
    if solve(line):
        print('yes')
    else:
        print('no')
