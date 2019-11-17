# https://www.acmicpc.net/problem/1912 문제 제목 : 연속합 , 언어 : Python, 날짜 : 2019-11-17, 결과 : 성공

import sys
n = int(sys.stdin.readline())
list_input = [0] + list(map(int, sys.stdin.readline().split()))#[input() for _ in range(n)]
list_dp = [0]*(n+1)
list_dp[1] = list_input[1]
max_value = -10000

if list_dp[1] > max_value:
	max_value = list_dp[1]
for i in range(2, n+1):
	if list_dp[i-1] < 0:
		list_dp[i] = list_input[i]
	else:
		list_dp[i] = list_input[i] + list_dp[i-1]
	if list_dp[i] > max_value:
		max_value = list_dp[i]
print(max_value)
