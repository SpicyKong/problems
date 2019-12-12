# https://www.acmicpc.net/problem/11048 문제 제목 : 이동하기 , 언어 : Python, 날짜 : 2019-12-12, 결과 : 성공

import sys
N, M = map(int, sys.stdin.readline().split())
list_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#list_dp = [[0]*(M+1) for _ in range(N+1)]
#list_dp[1][1] = list_map[0][]
for n in range(N):
    for m in range(M):
        if n == 0 and m == 0:
            pass
        elif n == 0:
            list_map[n][m]+=list_map[n][m-1]
        elif m == 0:
            list_map[n][m]+=list_map[n-1][m]
        else:
            list_map[n][m] += max(list_map[n][m-1], list_map[n-1][m], list_map[n-1][m-1])
print(list_map[N-1][M-1])
