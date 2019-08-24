# 푸는중..

import sys

N, M, K = map(int, sys.stdin.readline().split())

N_1 = N/2
N_2 , M_2 = 0,0
team_num = 0
if N_1 > M:
    team_num = M
    N_2 = (N_1 - M) * 2
elif N_1 < M:
    team_num = N_1
    M_2 = M - N_1
else:
    team_num = M
if K - N_2+M_2 < 0:
    K = 0
else:
    K-= N_2+M_2
a,b = divmod(K, 3)
if b>=1:
    a+=1
print(team_num)
