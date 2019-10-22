# https://www.acmicpc.net/problem/7569 문제 제목 : 토마토 , 언어 : Python, 날짜 : 2019-10-22, 결과 : 성공
# 이렇게 몇일이 지난건지 구하는 문제는 다른 분들의 코드를 보며 테크닉을 익혀야 할것같다.
# 이 코드도 좀더 간략하게 짜 보려다 BFS는 구현했지만 지난 날을 구하는 부분에서 계속 틀려서
# 하는수 없이 그냥 무식하게 짜게 되었다..


import sys
from collections import deque
M, N, H = map(int, sys.stdin.readline().split())
list_map = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
list_visit = [[[0]*M for _ in range(N)] for _ in range(H)]
list_queue1 = deque()
list_queue2 = deque()
count_tomato = 0
for h in range(H):
    for y in range(N):
        for x in range(M):
            if list_map[h][y][x] == 1:
                list_queue1.append([x,y,h])
                count_tomato += 1
ax = [1, -1, 0, 0, 0, 0]
ay = [0, 0, 1, -1, 0, 0]
ah = [0, 0, 0, 0, 1, -1]
day = 0
count_add = count_tomato
count_list = [count_tomato]
silheng1 = 0
silheng2 = 0
while  list_queue1 or  list_queue2:
    while list_queue1:
        silheng1 = 1
        dx, dy, dh = list_queue1.popleft()
        count_list[-1] -= 1
        list_map[dh][dy][dx] = 1
        for i in range(6):
            tx = dx + ax[i]
            ty = dy + ay[i]
            th = dh + ah[i]
            if 0 <= tx < M and 0 <= ty < N and 0 <= th < H:
                if list_visit[th][ty][tx] == 0 and list_map[th][ty][tx] == 0:
                    list_visit[th][ty][tx] = 1
                    list_queue2.append([tx, ty, th])
    if silheng1 == 1:
        day+=1
        silheng1 = 0
    while list_queue2:
        silheng2 = 1
        dx, dy, dh = list_queue2.popleft()
        count_list[-1] -= 1
        list_map[dh][dy][dx] = 1
        for i in range(6):
            if count_list[-1]==0:
                day+=1
            tx = dx + ax[i]
            ty = dy + ay[i]
            th = dh + ah[i]
            if 0 <= tx < M and 0 <= ty < N and 0 <= th < H:
                if list_visit[th][ty][tx] == 0 and list_map[th][ty][tx] == 0:
                    list_visit[th][ty][tx] = 1
                    list_queue1.append([tx, ty, th])
    if silheng2 == 1:
        day+=1
        silheng2 = 0



print_result = 0
for h in range(H):
    if print_result:
        break
    for y in range(N):
        if print_result:
            break
        for x in range(M):
            if list_map[h][y][x] == 0:
                print_result=1
                break
if print_result==1:
    print(-1)
else:
    print(day-1)
