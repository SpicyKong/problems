# https://www.acmicpc.net/problem/14502 문제 제목 : 연구소 , 언어 : Python, 날짜 : 2020-02-05, 결과 : 성공

import sys
from collections import deque


def bfs(list_map, n, m, virus, count, list_wall):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    list_queue = deque(virus)
    list_map_save = [a[:] for a in list_map]
    for location in list_wall:
        list_map_save[location[1]][location[0]] = 1
    while list_queue:
        now_x, now_y = list_queue.popleft()
        for i in range(4):
            nx = dx[i] + now_x
            ny = dy[i] + now_y
            if 0 <= nx < m and 0 <= ny < n:
                if not list_map_save[ny][nx]:
                    list_map_save[ny][nx] = 2
                    list_queue.append([nx, ny])
                    count -= 1
    #print(count)
    return count
    


N, M = map(int, sys.stdin.readline().split())
list_map = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
list_virus = []
count = 0
for y in range(N):
    for x in range(M):
        if list_map[y][x] == 2:
            list_virus.append([x, y])
        elif list_map[y][x] == 0:
            count += 1
result = 0
#bfs(list_map, N, M , list_virus, count)
list_locations = [[x, y] for x in range(M) for y in range(N) if not list_map[y][x]]
list_locations_length = len(list_locations)
for first in range(list_locations_length):
    for second in range(first+1, list_locations_length):
        for third in range(second+1, list_locations_length):
            save_count = bfs(list_map, N, M , list_virus, count, [list_locations[first], list_locations[second], list_locations[third]])
            if result < save_count:
                result = save_count
print(result-3)



