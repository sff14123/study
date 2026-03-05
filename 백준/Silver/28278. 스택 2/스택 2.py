import sys

# 입력을 빠르게 받기 위해 설정
input = sys.stdin.readline

# 1. 명령의 수 N을 입력받음
n = int(input())

# 2. 데이터를 담을 빈 리스트(스택) 생성
stack = []

# 3. N번만큼 반복하며 명령 처리
for _ in range(n):
    # 입력을 공백으로 나누어 리스트로 만듦 (예: "1 5" -> ["1", "5"])
    query = input().split()
    command = query[0]

    if command == '1':
        # 1 x: x를 스택에 넣는다
        stack.append(query[1])
        
    elif command == '2':
        # 2: 스택에 값이 있으면 빼서 출력, 없으면 -1
        if stack:
            print(stack.pop())
        else:
            print("-1")
            
    elif command == '3':
        # 3: 스택에 들어있는 정수의 개수 출력
        print(len(stack))
        
    elif command == '4':
        # 4: 스택이 비어있으면 1, 아니면 0 출력
        if not stack:
            print("1")
        else:
            print("0")
            
    elif command == '5':
        # 5: 스택에 값이 있으면 맨 위(마지막) 값 출력, 없으면 -1
        if stack:
            print(stack[-1])
        else:
            print("-1")