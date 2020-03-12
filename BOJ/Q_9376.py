# https://www.acmicpc.net/problem/9376 문제 제목 : 탈옥 , 언어 : Python, 날짜 : 2020-03-12, 결과 : 실패
"""
    회고:
    이 문제는 내일 풀고나서 회고를 작성하고 싶다.
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
