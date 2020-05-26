# https://www.acmicpc.net/problem/6593 문제 제목 : 상범 빌딩 , 언어 : Python, 날짜 : 2020-05-26, 결과 : 성공
"""
    회고:
    그냥 BFS문제인데 3차원이다. 3차원을 입력받는 문제라 그런지 조금 색다르게 느껴졌다.
    전형적인 BFS코드에서 3차원이니깐 두가지 방향(위, 아래)에 대한 행동만 추가해 주면 된다.
    
    오늘 파이썬 중간고사를 봤는데, 내가 파이썬을 자주 사용함에도 몇가지 제약이 있으니깐 생각보다 까다롭게 느껴졌다.
    파이썬 과목이니 만큼 좋은 결과가 있으면 좋겠다.
"""

import sys
from collections import deque

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

while True:
    L, R, C = map(int, sys.stdin.readline().split())
    if L==R==C==0:
        break
    list_map = [[list(sys.stdin.readline().strip()) for _ in range(R+1)] for _ in range(L)]
    list_visit = [[[0]*C for _ in range(R)] for _ in range(L)]
    for z in range(L):
        for y in range(R):
            for x in range(C):
                if list_map[z][y][x] == 'S':
                    start = (x,y,z)
                    list_visit[z][y][x] = 1
                elif list_map[z][y][x] == 'E':
                    end = (x,y,z)
    list_queue = deque()
    list_queue.append((start[0], start[1], start[2], 1))
    while list_queue:
        now_x, now_y, now_z, now_count = list_queue.popleft()
        for i in range(6):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            nz = now_z + dz[i]
            if 0<=nx<C and 0<=ny<R and 0<=nz<L:
                if not list_visit[nz][ny][nx] and not list_map[nz][ny][nx]=='#':
                    list_visit[nz][ny][nx] = now_count+1
                    list_queue.append((nx, ny, nz, now_count+1))
                    if (nx, ny, nz) == end:
                        list_queue=[]
                        break
    if list_visit[end[2]][end[1]][end[0]]:
        print('Escaped in', list_visit[end[2]][end[1]][end[0]]-1, 'minute(s).')
    else:
        print('Trapped!')
