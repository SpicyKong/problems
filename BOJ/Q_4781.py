# https://www.acmicpc.net/problem/4781 문제 제목 : 사탕 가게 , 언어 : Python, 날짜 : 2020-01-16, 결과 : 실패
# 파이썬으로 못푸는 문제인지 백준에선 파이썬 정답자가 한명밖에 없다.
# 시간될때 C로 다시 풀어봐야겠다.
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


