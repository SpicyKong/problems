# https://www.acmicpc.net/problem/2293 문제 제목 : 동전 1 , 언어 : Python, 날짜 : 2019-12-07, 결과 : 성공

import sys
n, k = map(int, sys.stdin.readline().split())
list_coin = [int(sys.stdin.readline()) for _ in range(n)]
list_dp = [0]*(k+1)
list_dp[0] = 1
for i in range(n):
    for j in range(list_coin[i], k+1):
        list_dp[j] += list_dp[j - list_coin[i]]
print(list_dp[k])
