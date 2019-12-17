# https://www.acmicpc.net/problem/10844 문제 제목 : 쉬운 계단 수 , 언어 : Python, 날짜 : 2019-12-17, 결과 : 성공

import sys
N = int(sys.stdin.readline())
list_dp = [[0]*(10),[0] + [1]*(9)] + [[0]*(10) for _ in range(N-1)]

for i in range(2, N +1):
    for j in range(10):
        if 1 <= j <= 8:
            list_dp[i][j] += list_dp[i-1][j-1] + list_dp[i-1][j+1]
        elif j == 0:
            list_dp[i][j] += list_dp[i-1][j+1]
        else:
            list_dp[i][j] += list_dp[i-1][j-1]
print(sum(list_dp[N])%1000000000)
