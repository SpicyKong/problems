# https://www.acmicpc.net/problem/2875 문제 제목 : 대회 or 인턴 , 언어 : Python, 날짜 : 2019-08-24, 결과 : 성공

import sys

N, M, K = map(int, sys.stdin.readline().split())
if N > 0 and M > 0:
    N_1 = N//2
    N_2, M_2 = 0, 0
    team_num = 0
    if N_1 > M:
        team_num += M
        N_2 = N - M*2
    elif N_1 < M:
        team_num += N_1
        M_2 = M - N_1
    else:
        team_num += M
    need = N_2+M_2
    if need >= K:
        K=0
    else:
        K = K-need
        a,b = divmod(K,3)
        if b >=1:
            a+=1
        team_num-=a
    print(team_num)
else:
    print(0)
