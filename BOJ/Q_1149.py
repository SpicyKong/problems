# https://www.acmicpc.net/problem/1149 문제 제목 : RGB거리 , 언어 : Python, 날짜 : 2019-11-28, 결과 : 성공

import sys

N = int(sys.stdin.readline())
list_fee = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# R G B
list_dp = [list_fee[0]] + [[0,0,0] for _ in range(N-1)]
for i in range(1,N):
    #list_fee[i]
    list_dp[i][0] = min(list_dp[i-1][1] , list_dp[i-1][2]) + list_fee[i][0]
    list_dp[i][1] = min(list_dp[i-1][0] , list_dp[i-1][2]) + list_fee[i][1]
    list_dp[i][2] = min(list_dp[i-1][0] , list_dp[i-1][1]) + list_fee[i][2]
print(min(list_dp[-1][0], list_dp[-1][1], list_dp[-1][2]))
