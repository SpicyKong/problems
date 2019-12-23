# https://www.acmicpc.net/problem/1890 문제 제목 : 점프 , 언어 : Python, 날짜 : 2019-12-23, 결과 : 성공

import sys
N = int(sys.stdin.readline())
list_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
list_dp = [[0]*N for _ in range(N)]
list_dp[0][0] = 1
for y in range(N):
    for x in range(N):
        num = list_map[y][x]
        if num:
            dy = [0, num]
            dx = [num, 0]
            for i in range(2):
                if 0 <= x + dx[i] < N and 0 <= y + dy[i] < N:
                    list_dp[y+dy[i]][x+dx[i]] += list_dp[y][x]
print(list_dp[N-1][N-1])

        
