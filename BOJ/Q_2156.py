# https://www.acmicpc.net/problem/2156 문제 제목 : 포도주 시식 , 언어 : Python, 날짜 : 2019-11-18, 결과 : 성공
# 내가 풀고 있는 DP문제들을 계속 반복문으로 구현하는데
# 내일 한번 재귀로도 풀어보아야 겠다.
import sys
N = int(sys.stdin.readline())
list_input =[0] + [int(sys.stdin.readline()) for _ in range(N)]
if N == 1:
    print(list_input[1])
elif N == 2:
    print(list_input[2] + list_input[1])
elif N == 3:
    print(max(list_input[1] + list_input[3], list_input[2] + list_input[3], list_input[1] + list_input[2]))
else:
    list_dp = [0]*(N+1)
    list_dp[1] = list_input[1]
    list_dp[2] = list_input[2] + list_input[1]
    list_dp[3] = max(list_input[1] + list_input[3], list_input[2] + list_input[3], list_input[1] + list_input[2])
    result_amount = 0
    for i in range(3, N+1):
        list_dp[i] = max(list_input[i] + list_dp[i-2], list_input[i] + list_input[i-1] + list_dp[i-3])
        list_dp[i] = max(list_dp[i-1], list_dp[i])
        if list_dp[i] > result_amount:
            result_amount = list_dp[i]
        
    print(result_amount)


"""

1 1 1 1 1 1
0 0 0 0 0 0
o x o
x o o 
6 10 13 9 8 1
x o o x o o x
o o x o x o o
"""
