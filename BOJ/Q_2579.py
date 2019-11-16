# https://www.acmicpc.net/problem/2579 문제 제목 : 계단 오르기 , 언어 : Python, 날짜 : 2019-11-16, 결과 : 성공
# 어떻게 이러한 생각이 도출되는건지.. 공부를 열심히 해야겠다.
import sys

N = int(sys.stdin.readline())

list_a = [0] + [int(sys.stdin.readline()) for _ in range(N)]

list_dp = [0]*(N+1)

list_dp[1] = list_a[1]
list_dp[2] = list_a[1] + list_a[2]



for i in range(3,N+1):
    list_dp[i] = max(list_dp[i-2] + list_a[i], list_dp[i-3] + list_a[i-1] + list_a[i])


print(list_dp[-1])
