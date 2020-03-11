# https://www.acmicpc.net/problem/17144 문제 제목 : 미세먼지 안녕! , 언어 : Python, 날짜 : 2020-03-10, 결과 : 성공
"""
    회고:
    구현만 하면 되는 문제다. 대부분의 구현 문제가 그렇듯이 문제 조건만 잘 보고 하라는대로만 하면 된다.
    아 근데 이 문제는 python3로 제출하니 시간초과가 떠서 pypy3로 제출했다. 아마도 모든맵을 일일이 돌면서
    확인하는부분을 최적화해야 파이썬으로도 통과가 되나보다.
"""
import sys
from collections import deque
R, C, T = map(int, sys.stdin.readline().split())
list_map = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]



def turn_on_cleaner():
    global list_map, info_air_cleaner, R, C
    for y in range(info_air_cleaner[0][1]-1,0,-1):
        list_map[y][0] = list_map[y-1][0]
    for y in range(info_air_cleaner[1][1]+1, R-1):
        list_map[y][0] = list_map[y+1][0]
    for x in range(C-1):
        list_map[0][x] = list_map[0][x+1]
        list_map[R-1][x] = list_map[R-1][x+1]
    for y in range(info_air_cleaner[0][1]):
        list_map[y][C-1] = list_map[y+1][C-1]
    for y in range(R-1, info_air_cleaner[0][1],-1):
        list_map[y][C-1] = list_map[y-1][C-1]
    for x in range(C-1,0,-1):
        list_map[info_air_cleaner[0][1]][x] = list_map[info_air_cleaner[0][1]][x-1]
        list_map[info_air_cleaner[1][1]][x] = list_map[info_air_cleaner[1][1]][x-1]
    list_map[info_air_cleaner[0][1]][1] = 0
    list_map[info_air_cleaner[1][1]][1] = 0



list_dust_queue = deque()
info_air_cleaner = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for y in range(R):
    for x in range(C):
        if list_map[y][x] == -1:
            info_air_cleaner.append([x,y])
        elif list_map[y][x]:
            list_dust_queue.append([x,y,list_map[y][x]])


for _ in range(T):
    while list_dust_queue:
        now_x, now_y, now_amount = list_dust_queue.popleft()
        count = 0
        for i in range(4):
            ny = now_y + dy[i]
            nx = now_x + dx[i]
            if 0 <= nx < C and 0 <= ny < R:
                if list_map[ny][nx]>=0:
                    list_map[ny][nx] += now_amount//5
                    count+=1
        list_map[now_y][now_x] -= now_amount//5*count
    turn_on_cleaner()
    result = 0
    for y in range(R):
        for x in range(C):
            if list_map[y][x] > 0:
                list_dust_queue.append([x, y,list_map[y][x]])
                result+=list_map[y][x]
print(result)
[print(a) for a in list_map]
