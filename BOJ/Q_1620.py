# https://www.acmicpc.net/problem/1620 문제 제목 : 나는야 포켓몬 마스터 이다솜 , 언어 : Python, 날짜 : 2019-09-26, 결과 : 성공

import sys
a = sys.stdin.readline
N, M = map(int, a().split())
c = {}
for i in range(1,N+1):
    n = a()[:-1]
    c[n] = str(i)
    c[str(i)] = str(n)
for _ in range(M):
    print(c[a()[:-1]])
