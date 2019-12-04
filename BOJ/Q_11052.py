# https://www.acmicpc.net/problem/11052 문제 제목 : 카드 구매하기 , 언어 : Python, 날짜 : 2019-12-04, 결과 : 성공
# 정말 오랜만에 DP문제중 검색찬스를 사용하지 않았다.
# 문제의 정답률과 상관없이 매우 기분이 좋다!ㅋㅋ

import sys
N = int(sys.stdin.readline())
list_a = [0] + list(map(int, sys.stdin.readline().split()))
list_dp = [0] * (N+1)
list_dp[1] = list_a[1]
for i in range(2, N+1):
    test = 0
    for j in range(1,i+1):
        if list_dp[i-j] + list_a[j] > test:
            test = list_dp[i-j] + list_a[j]
    list_dp[i] = test
print(list_dp[-1])
"""

1 5 6 7

0 1 2 3 4 5 6 7 8 9 10
0 1 5 6 10

"""
