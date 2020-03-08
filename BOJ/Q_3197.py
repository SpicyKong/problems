# https://www.acmicpc.net/problem/3197 문제 제목 : 백조의 호수 , 언어 : Python, 날짜 : 2020-03-08, 결과 : 실패
"""
    회고:
    당연히 이렇게 짜면 틀릴거 같았지만 역시나 틀렸다. 다른분들의 풀이를 살펴보니 BFS를 최소한 돌려서 푸시던데
    한번 생각해봐야겠다. 아 그리고 지금 코드가 굉장히 복잡한데 맨처음에는 백조에 대해서 BFS돌리는 함수와
    얼음이 녹는 함수를 구현해두었는데 메모리초과가 떠서 혹시나해서 함수 호출과정이 없는코드로 바꾸어 보았는데
    크게 의미없었다.

    P.S.
    스트레스를 풀만한 취미를 하나 찾아야겠다. 어정쩡하게 무의미한 시간을 보내니 프로그래밍에 집중도 안되고
    그렇다고 휴식이 되지도 않는다. 오늘은 하루 쉬는 하루였다고 생각하고 내일부턴 다시 규칙적으로 공부해야겠다.
"""

import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
list_map = [list(sys.stdin.readline()) for _ in range(R)]

list_ice_queue = deque()
count_ice = 0
list_swan = []
list_queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for y in range(R):
    for x in range(C):
        if list_map[y][x] == 'X':
            list_ice_queue.append([x,y])
            count_ice+=1
        elif list_map[y][x] == 'L':
            list_swan.append([x,y])


list_visit = [[0]*C for _ in range(R)]
day = 1
end = 0
while True:
    list_queue.append(list_swan[0])
    list_visit[list_swan[0][1]][list_swan[0][0]] = day
    while list_queue:
        now_x, now_y = list_queue.popleft()
        for i in range(4):
            nx = dx[i] + now_x
            ny = dy[i] + now_y
            if 0 <= nx < C and 0 <= ny < R:
                if list_map[ny][nx] == '.' and list_visit[ny][nx] < day:
                    list_visit[ny][nx] = day
                    list_queue.append([nx, ny])
                elif list_map[ny][nx] == 'L' and list_visit[ny][nx] < day:
                    end = 1
                    list_queue=[]
                    break
    if end:
        print(day-1)
        break

    save_count = 0
    save_xy = []
    while list_ice_queue and count_ice>0:
        now_x, now_y = list_ice_queue.popleft()
        count_ice-=1
        token = 1
        for i in range(4):
            nx = dx[i] + now_x
            ny = dy[i] + now_y
            if 0 <= nx < C and 0 <= ny < R:
                if list_map[ny][nx] == '.' or list_map[ny][nx] == 'L':
                    save_xy.append([now_x,now_y])
                    token = 0
                    break
        if token:
            list_ice_queue.append([now_x, now_y])
            save_count+=1
    while save_xy:
        x, y = save_xy.pop()
        list_map[y][x] = '.'
    count_ice = save_count
    day+=1
