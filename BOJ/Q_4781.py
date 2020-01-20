# https://www.acmicpc.net/problem/4781 문제 제목 : 사탕 가게 , 언어 : Python, 날짜 : 2020-01-16, 결과 : 실패(시간초과)
# https://www.acmicpc.net/problem/4781 문제 제목 : 사탕 가게 , 언어 : Python, 날짜 : 2020-01-20, 결과 : 성공

import sys

while True:
    n, m = map(float, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    m = round(m*100)
    list_dp = [0]*(m+1)
    

    iteration_count = 0
    while n > iteration_count:
        c, p = map(float, sys.stdin.readline().split())
        p = round(p*100)
        for i in range(p, m+1):
            list_dp[i] = max(list_dp[i], list_dp[i - p] + c)
        iteration_count+=1
    print(int(list_dp[-1]))



# 실패코드
import sys

input_a = sys.stdin.readline
while True:
    n, m = map(float, input_a().split())
    n,m = int(n), round(m*100 + 0.5)
    num_max = 0
    if n == 0 and m == 0:
        break
    list_input = []
    asdf = list_input.append
    list_dp = [0]*(m+1)

    for _ in range(n):
        c, p = map(float, input_a().split())
        c, p = int(c), round(p*100 + 0.5)
        list_dp[p] = c
        asdf([c,p])
    for i in range(1,m):
        if list_dp[i]:
            for list_cp in list_input:
                if i + list_cp[1] <= m and list_dp[i] + list_cp[0] > list_dp[i + list_cp[1]]:
                    list_dp[list_cp[1] + i] = list_dp[i] + list_cp[0]
                    if list_dp[list_cp[1] + i] > num_max:
                        num_max = list_dp[list_cp[1] + i]
    print(num_max)


