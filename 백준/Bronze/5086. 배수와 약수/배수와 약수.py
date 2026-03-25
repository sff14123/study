import sys

while True:
    line = sys.stdin.readline().split()
    if not line: break  # 더 이상 읽을 내용이 없으면 종료
    
    n1, n2 = map(int, line)
    
    if n1 == 0 and n2 == 0:
        break
        
    if n1 != 0 and n2 % n1 == 0: # n1이 0인 경우를 대비한 안전장치
        print('factor')
    elif n2 != 0 and n1 % n2 == 0:
        print('multiple')
    else:
        print('neither')