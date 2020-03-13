# https://www.acmicpc.net/problem/9376 문제 제목 : 탈옥 , 언어 : Python, 날짜 : 2020-03-12, 결과 : 실패
"""
    회고:
    이 문제는 내일 풀고나서 회고를 작성하고 싶다.
    밑에 회고 작성했다.
"""
import sys
from collections import deque
list_result = []
T = int(sys.stdin.readline())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(T):
    h, w = map(int, sys.stdin.readline().split())
    list_map = [list(sys.stdin.readline().strip()) for _ in range(h)]
    list_visit = [[[0,0] for _ in range(w)] for _ in range(h)]
    list_xy=[]
    for y in range(h):
        for x in range(w):
            if list_map[y][x] == '$':
                list_xy.append([x,y])
    
    list_queue1 = deque([[*list_xy[0],0,[]]])
    result1 = []
    list_queue2 = deque([[*list_xy[1],0,[]]])
    result2 = []

    while list_queue1:
        now_x, now_y,count_key, now_door = list_queue1.popleft()
        if now_x==0 or now_y==0 or now_x==w-1 or now_y==h-1:
            result1.append(now_door)
        else:
            for i in range(4):
                #print('=======================')
                #[print(a) for a in list_visit]
                nx = dx[i] + now_x
                ny = dy[i] + now_y
                if (list_map[ny][nx] == '.' or list_map[ny][nx] == '$') and not list_visit[ny][nx][0] == 1:
                    list_queue1.append([nx, ny, count_key, now_door])
                    list_visit[ny][nx][0] = 1
                    list_visit[ny][nx][1] = count_key
                elif list_map[ny][nx] == '#' and not list_visit[ny][nx][0] == 1:
                    list_queue1.append([nx, ny, count_key+1, now_door+[[nx,ny]]])
                    list_visit[ny][nx][0] = 1
                    list_visit[ny][nx][1] = count_key+1
                elif (list_map[ny][nx] == '.' or list_map[ny][nx] == '$') and list_visit[ny][nx][0] == 1 and list_visit[ny][nx][1] > count_key:
                    list_queue1.append([nx, ny, count_key, now_door])
                    list_visit[ny][nx][1] = count_key
                elif list_map[ny][nx] == '#' and list_visit[ny][nx][0] == 1 and list_visit[ny][nx][1] > count_key+1:
                    list_queue1.append([nx, ny, count_key+1, now_door+[[nx,ny]]])
                    list_visit[ny][nx][0] = 1
                    list_visit[ny][nx][1] = count_key+1
    while list_queue2:
        now_x, now_y,count_key, now_door = list_queue2.popleft()
        if now_x==0 or now_y==0 or now_x==w-1 or now_y==h-1:
            result2.append(now_door)
        else:
            for i in range(4):
                nx = dx[i] + now_x
                ny = dy[i] + now_y
                if (list_map[ny][nx] == '.' or list_map[ny][nx] == '$') and not list_visit[ny][nx][0] == 2:
                    list_queue2.append([nx, ny, count_key, now_door])
                    list_visit[ny][nx][0] = 2
                    list_visit[ny][nx][1] = count_key
                elif list_map[ny][nx] == '#' and not list_visit[ny][nx][0] == 2:
                    list_queue2.append([nx, ny, count_key+1, now_door+[[nx,ny]]])
                    list_visit[ny][nx][0] = 2
                    list_visit[ny][nx][1] = count_key+1
                elif (list_map[ny][nx] == '.' or list_map[ny][nx] == '$') and list_visit[ny][nx][0] == 2 and list_visit[ny][nx][1] > count_key:
                    list_queue2.append([nx, ny, count_key, now_door])
                    list_visit[ny][nx][1] = count_key
                elif list_map[ny][nx] == '#' and list_visit[ny][nx][0] == 2 and list_visit[ny][nx][1] > count_key+1:
                    list_queue2.append([nx, ny, count_key+1, now_door+[[nx,ny]]])
                    list_visit[ny][nx][0] = 2
                    list_visit[ny][nx][1] = count_key+1
    check = -1
    result = 10000+1
    for key1 in result1:
        for key2 in result2:
            count=0
            for key_x, key_y in key1:
                list_map[key_y][key_x] = check
                count+=1
            for key_x, key_y in key2:
                if not list_map[key_y][key_x] == check:
                    count+=1
            if result>count:
                result=count
            check-=1
    #print(result)
    list_result.append(result)
[print(a) for a in list_result]
#####################################################################################################
# https://www.acmicpc.net/problem/9376 문제 제목 : 탈옥 , 언어 : Python, 날짜 : 2020-03-13, 결과 : 성공
"""
    회고:
    결국 다른분의 코드를 참고했다. 하지만 다른분의 코드를 이해하는데에도 오래걸렸다..
    먼저 기본적인 아이디어인 bfs를 해주며 visit에 지나온 문의 개수를 카운팅해주는 방법은 기존에 내가 생각했던 방법과 유사했다.
    하지만 맵의 테두리에 .(빈공간)을 추가하고 (0,0)에서 bfs를 추가한 뒤 3군데에서 BFS를 돌릴생각은 하지 못했다..
    이 방법의 장점은 항상 자신의 위치 기준으로 지나온 비용, 다른 탈옥수를 데리러 가는 비용, 앞으로 필요한 비용을 계산하기가 수월하다는것이다.
    세상에는 정말 대단하신 분들이 많은것 같다..ㅠㅠ
"""

import sys
from collections import deque


def bfs(fx, fy):
    list_visit = [[-1]*(w+2) for _ in range(h+2)]
    list_visit[fy][fx] = 0
    list_queue = deque()
    list_queue.append([fx, fy,0])
    while list_queue:
        now_x, now_y,now_count = list_queue.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0 <= nx <= w+1 and 0 <= ny <= h+1:
                if (list_map[ny][nx] == '.' or list_map[ny][nx] == '$') and list_visit[ny][nx] == -1:
                    list_queue.append([nx,ny,now_count])
                    list_visit[ny][nx] = now_count
                elif list_map[ny][nx] == '#' and list_visit[ny][nx] == -1:
                    list_queue.append([nx,ny,now_count+1])
                    list_visit[ny][nx] = now_count+1
                elif (list_map[ny][nx] == '.' or list_map[ny][nx] == '$') and list_visit[ny][nx] > now_count:                
                    list_queue.append([nx,ny,now_count])
                    list_visit[ny][nx] = now_count
                elif list_map[ny][nx] == '#' and list_visit[ny][nx] > now_count+1:
                    list_queue.append([nx,ny,now_count+1])
                    list_visit[ny][nx] = now_count+1
    return list_visit

dx = [1,-1,0,0]
dy = [0,0,1,-1]
T = int(sys.stdin.readline())
for _ in range(T):
    h, w = map(int, sys.stdin.readline().split())
    list_map = []
    list_map.append(['.']*(w+2))
    for _ in range(h):
        imsi_input = list(sys.stdin.readline().strip())
        list_map.append(['.'] + imsi_input +['.'])
    list_map.append(['.']*(w+2))
    list_talok = []
    for y in range(h+2):
        for x in range(w+2):
            if list_map[y][x] == '$':
                list_talok.append([x, y])
    imsi_map1 = bfs(0, 0)
    imsi_map2 = bfs(list_talok[0][0], list_talok[0][1])
    imsi_map3 = bfs(list_talok[1][0], list_talok[1][1])
    result = 10000000000
    for y in range(h+2):
        for x in range(w+2):
            if not list_map[y][x] == '*':
                imsi_sum = imsi_map1[y][x] + imsi_map2[y][x] + imsi_map3[y][x]
                if list_map[y][x] == '#':
                    imsi_sum-=2
                if result > imsi_sum:
                    result = imsi_sum
    print(result)
