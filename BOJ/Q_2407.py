# https://www.acmicpc.net/problem/2407 문제 제목 : 조합 , 언어 : Python, 날짜 : 2019-11-21, 결과 : 성공
# 파이썬이라 쉽게 풀린거같다.

import sys

n, m = map(int, sys.stdin.readline().split())
result = n
for i in range(1,m):
    result*=(n-i)
for i in range(1,m): 
    result//=(m -i +1)
print(result)
