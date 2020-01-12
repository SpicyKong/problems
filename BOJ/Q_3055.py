# https://www.acmicpc.net/problem/3055 문제 제목 : 탈출 , 언어 : Python, 날짜 : 2020-01-13, 결과 : 성공
# 아침에 일어나면 놀러가야되서 문제를 못풀기때문에 새벽에 
# 푸는데 오늘은 영 푸는날이 아닌것같다
# 너무 창피한 코드를 작성했따.
# 나중에 다시 짜야겠다.

import sys
from collections import deque
R, C = map(int, sys.stdin.readline().split())

list_map = [list(sys.stdin.readline().strip()) for _ in range(R)]
list_visit = [[0]*C for _ in range(R)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
list_water= deque()

for y in range(R):
    for x in range(C):
        if list_map[y][x] == 'D':
            goal = [x, y]
        elif list_map[y][x] == 'S':
            now = [x, y]
            list_visit[y][x] = 1
        elif list_map[y][x] == 'X':
            list_visit[y][x] = -1
        elif list_map[y][x] == '*':
            list_visit[y][x] = -1

            list_water.append([x, y])


list_queue = deque([now])
count_queue = [1]
minute = 0


end = 0
normal_ending = 1
while not end:
    list_water_save = []
    while list_water:
        water_x, water_y = list_water.popleft()
        for i in range(4):
            new_water_x = water_x + dx[i]
            new_water_y = water_y + dy[i]
            if 0 <= new_water_x < C and 0 <= new_water_y < R:
                if not list_visit[new_water_y][new_water_x] == -1 and not [new_water_x, new_water_y] == goal:
                    list_visit[new_water_y][new_water_x] = -1
                    list_water_save.append([new_water_x, new_water_y])
    list_water = deque(list(list_water_save))

    list_save = []
    while list_queue:
        add1 = 0
        now_x, now_y = list_queue.popleft()
        if [now_x, now_y] == goal:
            end = 1
            add1 += 1
            list_save = [[456]]
            break
        for i in range(4):
            new_x = now_x + dx[i]
            new_y = now_y + dy[i]
            if 0 <= new_x < C and 0 <= new_y < R:
                if not list_visit[new_y][new_x]:
                    list_visit[new_y][new_x] = 1
                    list_save.append([new_x, new_y])
                    add1+=1
    list_queue = deque(list(list_save))
    if not list_save:
        normal_ending = 0
        end = 1
    
    
    minute += 1
if normal_ending:
    print(minute - 1)
else:
    print("KAKTUS")
