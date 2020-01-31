# https://www.acmicpc.net/problem/2206 문제 제목 : 벽 부수고 이동하기 , 언어 : Python, 날짜 : 2020-01-31, 결과 : 성공
"""
두 테스트 케이스 덕분에 오류를 찾을 수 있었다.

5 5
01100
01000
01110
01000
00010

4 4
0101
0101
0001
1110
"""

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
list_map = [list(sys.stdin.readline().strip()) for _ in range(N)]
list_visit = [[0]*M for _ in range(N)]
list_queue = deque()
list_queue.append([0,0,0,1]) # x, y, 벽, count
for y in range(N):
    for x in range(M):
        if list_map[y][x] == '1':
            list_visit[y][x] = -1
list_visit[0][0] = [0,0,0,1]
dy = [0,0,1,-1]
dx = [1,-1,0,0]

while list_queue:
    
    
    
    x, y, is_wall_break, count = list_queue.popleft()
    if x == M-1 and y == N-1:
        break
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < M and 0 <= next_y < N:
            try:
                if list_visit[next_y][next_x] == 0:
                    list_save = [next_x, next_y, is_wall_break, count+1]
                    list_visit[next_y][next_x] = list_save
                    list_queue.append(list_save)
                elif list_visit[next_y][next_x] == -1 and not is_wall_break:
                    list_queue.append([next_x, next_y, 1, count+1])
                    list_visit[next_y][next_x]-=1
                elif not list_visit[next_y][next_x] == -2 and not is_wall_break and list_visit[next_y][next_x][2] == 1:
                    list_save = [next_x, next_y, is_wall_break, count+1]
                    list_visit[next_y][next_x] = list_save
                    list_queue.append(list_save)
            except:
                print(list_visit[next_y][next_x])
                

if list_visit[N-1][M-1]:
    print(list_visit[N-1][M-1][3])
else:
    print(-1)
