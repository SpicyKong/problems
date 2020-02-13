# https://www.acmicpc.net/problem/1981 문제 제목 : 배열에서 이동 , 언어 : Python, 날짜 : 2020-02-13, 결과 : 실패
# 맞왜틀..

import sys
from collections import deque

N = int(sys.stdin.readline())
list_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
list_visit = [[0]*N for _ in range(N)] # 방문을 체크하는 동시에 방문을 했다면 [최소, 최대, 차]값을 저장하는 2차원 리스트입니다.

list_queue = deque([[0,0,list_map[0][0],list_map[0][0],207]]) # [x좌표, y좌표, 현재 최소값, 현재 최대값, 차]를 저장하고 BFS에 이용하는 큐입니다.
list_visit[0][0] = [list_map[0][0],list_map[0][0],201] # 방문을 체크할때 옆과같이 [최소, 최대, 차]값을 저장해 둡니다. 200이 문제에서 나올수있는 차의 최댓값이기 때문에 그보다 큰 201로 초기화.
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while list_queue:
    now_x, now_y, now_min, now_max, now = list_queue.popleft()
    print("=============")
    [print(a) for a in list_visit]
    for i in range(4):
        nx = now_x + dx[i]
        ny = now_y + dy[i]
        if 0 <= nx < N and 0 <= ny < N: # 리스트의 범위를 벗어 나지 않는다면
            nmin = min(now_min, list_map[ny][nx]) # 현재 최소값
            nmax = max(now_max, list_map[ny][nx]) # 현재 최대값
            if not list_visit[ny][nx]: # 이동하려는 칸이 방문한적이 없었다면
                list_visit[ny][nx] = [nmin, nmax, nmax-nmin] # 방문체크
                list_queue.append([nx, ny, nmin, nmax, nmax-nmin]) # 큐에 값을 넣어줌
            elif list_visit[ny][nx][2] > nmax - nmin: # 방문을 했었지만, 차의값을 줄일수있는 경로라면
                list_visit[ny][nx] = [nmin, nmax, nmax-nmin] # 방문체크된 값을 새롭게 저장
                list_queue.append([nx, ny, nmin, nmax, nmax-nmin]) # 큐에 값을 넣어줌
print(list_visit[N-1][N-1][2])






"""
4 3 3 5 5
3 9 9 9 9
3 9 2 2 3
4 9 1 9 2
5 4 3 9 0

5
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 10
0 0 0 10 200

7
1 1 1 7 1 1 1
1 5 1 6 1 1 1
1 5 1 5 1 4 1
1 5 1 4 1 5 1
1 5 1 3 1 6 1
1 5 1 2 1 8 1
1 5 1 0 1 9 1

"""

        
