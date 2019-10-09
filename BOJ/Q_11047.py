# https://www.acmicpc.net/problem/11047 문제 제목 : 동전 0 , 언어 : Python, 날짜 : 2019-10-09, 결과 : 성공

import sys
N, K = map(int, sys.stdin.readline().split())
result = 0
list_a = [int(sys.stdin.readline()) for _ in range(N)]
for i in range(N):
    price = list_a[-1-i]
    if price <= K:
        q = K//price
        result += q
        K -= q*price
print(result)
