# https://www.acmicpc.net/problem/11053 문제 제목 : 가장 긴 증가하는 부분 수열 , 언어 : Python, 날짜 : 2019-10-10, 결과 : 성공

import sys

N = int(sys.stdin.readline())

list_a = list(map(int, sys.stdin.readline().split()))
list_dp = [1] + [1]*(N-1)
max_num = 1
for i in range(N):
    for j in range(0,i+1):
        if list_a[i] > list_a[j] and list_dp[i] < list_dp[j] + 1:
            list_dp[i] = list_dp[j] + 1
            if list_dp[i] > max_num:
                max_num = list_dp[i]
print(max_num)
