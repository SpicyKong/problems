# https://www.acmicpc.net/problem/4179 문제 제목 : 불! , 언어 : Python, 날짜 : 2020-01-25, 결과 : 성공
# 코드가 더럽다..
# 좀 정리하면서 짜야하는데 설날이라 시간이 많이 없다


import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
list_map = [list(sys.stdin.readline().strip()) for _ in range(R)]
list_visit = [[0]*C for _ in range(R)]
list_count_f = [0]
list_fire = deque()
list_queue = deque()
list_count = [1]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
True_end = 0
count_j = 0
count_f = 0
time_escape = 0
for y in range(R):
    for x in range(C):
        if list_map[y][x] == 'J':
            list_queue.append([x, y])
            list_visit[y][x] = 1
        elif list_map[y][x] == '#':
            list_visit[y][x] = -1
        elif list_map[y][x] == 'F':
            list_visit[y][x] = 2
            list_count_f[0] += 1
            list_fire.append([x, y])



while list_fire:
    if not list_count_f[-1]:
        list_count_f.append(count_f)
        count_f = 0
        break
    now_x_f, now_y_f = list_fire.popleft()
    list_count_f[-1] -= 1
    for j in range(4):
        imsi_x_f = dx[j] + now_x_f
        imsi_y_f = dy[j] + now_y_f
        if 0 <= imsi_x_f < C and 0 <= imsi_y_f < R:
            if not list_visit[imsi_y_f][imsi_x_f] or list_visit[imsi_y_f][imsi_x_f]==1:
                list_visit[imsi_y_f][imsi_x_f] = 2
                list_fire.append([imsi_x_f, imsi_y_f])
                count_f += 1

while list_queue:
    #print("=============")
    #print(time_escape)
    #[print(a) for a in list_visit]

    if not list_count[-1]:
        list_count.append(count_j)
        count_j = 0
        time_escape += 1
        while list_fire:
            if not list_count_f[-1]:
                list_count_f.append(count_f)
                count_f = 0
                break
            now_x_f, now_y_f = list_fire.popleft()
            list_count_f[-1] -= 1
            for j in range(4):
                imsi_x_f = dx[j] + now_x_f
                imsi_y_f = dy[j] + now_y_f
                if 0 <= imsi_x_f < C and 0 <= imsi_y_f < R:
                    if not list_visit[imsi_y_f][imsi_x_f] or list_visit[imsi_y_f][imsi_x_f]==1:
                        list_visit[imsi_y_f][imsi_x_f] = 2
                        list_fire.append([imsi_x_f, imsi_y_f])
                        count_f += 1
    now_x, now_y = list_queue.popleft()
    list_count[-1] -= 1
    if now_x == 0 or now_y == 0 or now_x == C - 1 or now_y == R - 1:
        True_end = 1
        break
    
        
        
    for i in range(4):
        imsi_x = dx[i] + now_x
        imsi_y = dy[i] + now_y
        if 0 <= imsi_x < C and 0 <= imsi_y < R:
            #print(list_map[imsi_y][imsi_x])
            if not list_visit[imsi_y][imsi_x]:
                list_visit[imsi_y][imsi_x] = 1
                list_queue.append([imsi_x, imsi_y])
                count_j += 1
if True_end:
    print(time_escape + 1)
else:
    print("IMPOSSIBLE")
