# https://www.acmicpc.net/problem/11967 문제 제목 : 불켜기 , 언어 : Python, 날짜 : 2020-01-28, 결과 : 성공
# 이 문제는 두번쨰 while문에서 이상한 조건을 넣어버려서 계속 틀렸다..

import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
list_map = [[0]*(N+1) for _ in range(N+1)]
list_lights = [[0]*(N+1) for _ in range(N+1)]

count_light = 1
for _ in range(M):
    x,y,a,b = map(int,sys.stdin.readline().split())
    if not list_map[y][x]:
        list_map[y][x] = [[a,b]]
    else:
        list_map[y][x].append([a,b])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
list_lights[1][1] = 1
while True:
    list_visit = [[0]*(N+1) for _ in range(N+1)]
    list_visit[1][1] = 1
    save_count = count_light
    list_queue = deque([[1,1]])
    while list_queue:
        now_x, now_y = list_queue.popleft()
        if list_map[now_y][now_x]:
            while list_map[now_y][now_x]:
                light_x, light_y = list_map[now_y][now_x].pop()
                if not list_lights[light_y][light_x]:
                    list_lights[light_y][light_x] = 1
                    count_light+=1
        for i in range(4):
            test_x = dx[i] + now_x
            test_y = dy[i] + now_y
            if 0 < test_x <= N and 0 < test_y <= N:
                if list_lights[test_y][test_x] and not list_visit[test_y][test_x]:
                    list_visit[test_y][test_x] = 1
                    list_queue.append([test_x, test_y])

    if save_count == count_light:
        break
print(count_light)
