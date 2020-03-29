# https://www.acmicpc.net/problem/4963 문제 제목 : 섬의 개수 , 언어 : Python, 날짜 : 2020-03-30, 결과 : 성공 
"""
    회고:
    그냥 새로운 섬 만날떄마다 체크해주면 된다.
    이제는 골드문제 아닌것들도 풀어봐야겠다. 골드문제 너무 어렵다..ㅠㅠ
"""

import sys
from collections import deque

def bfs(x,y,w,h):
    list_queue = deque()
    list_queue.append([x,y])
    while list_queue:
        now_x, now_y = list_queue.popleft()
        for i in range(8):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0 <= nx < w and 0 <= ny < h:
                if list_map[ny][nx] == 1 and not list_visit[ny][nx]:
                    list_visit[ny][nx] = 1
                    list_queue.append([nx,ny])


dx = [1,1,1,0,-1,-1,-1,0]
dy = [1,0,-1,-1,-1,0,1,1]
while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    list_map = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    list_visit = [[0]*w for _ in range(h)]
    count = 0
    for y in range(h):
        for x in range(w):
            if list_map[y][x] == 1 and not list_visit[y][x]:
                count+=1
                bfs(x,y,w,h)
    print(count)
