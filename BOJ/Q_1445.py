# https://www.acmicpc.net/problem/1445 문제 제목 : 일요일 아침의 데이트 , 언어 : Python, 날짜 : 2020-05-20, 결과 : 성공
"""
    회고:
    그냥 BFS문제다. 약간 다른점은 거리상의 최단경로를 구하는것이 아니라 조건에 따른 최적의 경로를 구하는 것이기때문에
    방문체크를 하는게 아니라 가도 되는지만 확인하면 된다. 아 그리고 나는 문자열이 싫어서 전처리를 해주었다.
"""

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
list_map = [list(sys.stdin.readline().strip()) for _ in range(N)]
list_visit = [[[3000,3000] for _ in range(M)] for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
fxy = [0,0]
sxy = [0,0]
for y in range(N):
    for x in range(M):
        if list_map[y][x] == '.':
            list_map[y][x] = 0
        elif list_map[y][x] == 'g':
            list_map[y][x] = 1
            for i in (0, 1, 2, 3):
                if 0<=x+dx[i]<M and 0<=y+dy[i]<N and (list_map[y+dy[i]][x+dx[i]]=='.' or list_map[y+dy[i]][x+dx[i]]==0):
                    list_map[y+dy[i]][x+dx[i]] = -1
        elif list_map[y][x] == 'S':
            sxy = [x, y]
            list_map[y][x] = 2
            list_visit[y][x] = [0,0]
        elif list_map[y][x] == 'F':
            fxy = [x, y]
            list_map[y][x] = 3

list_queue = deque()
list_queue.append((sxy[0], sxy[1], 0, 0))
while list_queue:
    now_x, now_y, now_g, now_gp = list_queue.popleft()
    if now_x==fxy[0] and now_y==fxy[1] and now_g==0 and now_gp==0:
        break
    for i in (0, 1, 2, 3):
        nx = now_x+dx[i]
        ny = now_y+dy[i]
        if 0<=nx<M and 0<=ny<N:
            next_g, next_gp = now_g, now_gp
            if list_map[ny][nx] == 1:
                next_g+=1
            elif list_map[ny][nx] == -1:
                next_gp+=1
            if list_visit[ny][nx] > [next_g, next_gp]:
                list_visit[ny][nx] = [next_g, next_gp]
                list_queue.append((nx, ny, next_g, next_gp))                
print(*list_visit[fxy[1]][fxy[0]])
"""
3 5
...F.
ggggg
...S.
"""
