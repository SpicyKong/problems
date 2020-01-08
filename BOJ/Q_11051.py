# https://www.acmicpc.net/problem/11051 문제 제목 : 이항 계수 2 , 언어 : Python, 날짜 : 2020-01-08, 결과 : 성공

import sys

N, K = map(int, sys.stdin.readline().split())
list_memo = [[0] * (i + 1) if i < K else [0] * (K + 1) for i in range(N+1)]
for n in range(N+1):
    if n > K:
        c = K
    else:
        c = n
    for r in range(c+1):
        #print(n, r)
        if r == 0 or r == n:
            list_memo[n][r] = 1
        else:    
            #print(n,r)
            list_memo[n][r] = list_memo[n-1][r-1] + list_memo[n-1][r]
print(list_memo[N][K]%10007)
