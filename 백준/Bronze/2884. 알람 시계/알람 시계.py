H, M = map(int, input().split())
minute = H*60 + M
alram = minute - 45
N_H, N_M = alram // 60, alram % 60
if N_H < 0:
    N_H = 24 + N_H
print(N_H, N_M)