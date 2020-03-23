# https://www.acmicpc.net/problem/16933 문제 제목 : 벽 부수고 이동하기 3 , 언어 : Python, 날짜 : 2020-03-23, 결과 : 성공
"""
    회고:
    문제의 접근은 벽 부수고 이동하기 문제와 비슷하다 다만 낮과 밤이 추가되었다는점만 다르다.
    단순히 큐에 낮과 밤을 체크하는 부분을 넣어주면 된다.
    
    내가 실수했던 부분들:
    1. visit을 체크하는 배열을 처음에 [[],[],[], ... ,[]] 이런식으로 선언했다. 아마도 이런식으로 선언해두는건 연산속도가 빠르지는 않나보다.
    2. 만약 지금 시간이 밤이면 count+2하고 그냥 이동시켜줬다. 이 경우는 왜 문제가 된건지 아직은 짐작이 안되지만 분명 내가 생각하지 못한 반례가 있을것이다.
    
    어렵진 않았던 문제인데 제출을 너무 많이 했다. 아쉽다.
    아 그리고 이 코드는 pypy3로 제출했다.
"""

import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]
N, M, K = map(int, sys.stdin.readline().split())
list_map = [list(sys.stdin.readline().strip()) for _ in range(N)]
list_visit = [[[0,0] for _ in range(M)] for _ in range(N)]
list_queue = deque()
list_queue.append([0,0,1,1,K]) # x, y, count, day, K ||||||||||||| day = 1 night = -1
list_visit[0][0] = [1,K]

while list_queue:
    #print(list_queue)
    now_x, now_y, now_count, day, now_k = list_queue.popleft()
    if now_y==N-1 and now_x==M-1:
        break
    for i in range(4):
        nx = now_x + dx[i]
        ny = now_y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if list_map[ny][nx] == '0' and (not list_visit[ny][nx][0] or list_visit[ny][nx][1] < now_k):
                list_queue.append([nx, ny, now_count+1, day*-1, now_k])
                list_visit[ny][nx][0] = now_count+1
                list_visit[ny][nx][1] = now_k
            elif list_map[ny][nx] == '1' and now_k and (not list_visit[ny][nx][0] or list_visit[ny][nx][1] < now_k):
                if day>0:
                    list_queue.append([nx, ny, now_count+1, day*-1, now_k-1])
                    list_visit[ny][nx][0] = now_count+1
                    list_visit[ny][nx][1] = now_k-1
                else:
                    list_queue.append([now_x, now_y, now_count+1, day*-1, now_k])
if list_visit[N-1][M-1][0]:
    print(list_visit[N-1][M-1][0])
else:
    print(-1)
