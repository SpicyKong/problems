# https://www.acmicpc.net/problem/1915 문제 제목 : 가장 큰 정사각형 , 언어 : Python, 날짜 : 2019-12-16, 결과 : 성공

import sys


n,m = map(int, sys.stdin.readline().split())
list_a = [[0]*(m+1)] + [[0]+list(map(int, list(sys.stdin.readline()[:-1]))) for _ in range(n)]

result = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if list_a[i][j]:

            list_a[i][j] += min(list_a[i-1][j-1], list_a[i-1][j], list_a[i][j-1])
            if list_a[i][j] > result:
                result = list_a[i][j]
print(result**2)
