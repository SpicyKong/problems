# https://www.acmicpc.net/problem/16236 문제 제목 : 아기 상어 , 언어 : Python, 날짜 : 2020-03-09, 결과 : 성공

import sys
from collections import deque
"""
    회고:
    문제를 잘못해석 해서 총 3번 다시 풀게 되었다.
    맨 처음엔 자신의 크기 이하의 지역만 지나갈수있다는 조건을 보지 못했고,
    두번째 시도에는 우선순위를 잘못 보았다. 
    그래서 우선순위에 대한 단서를 다시 읽고 문제를 풀어나가는데 생각보다 귀찮았다.
    그래도 구현이 어려운 문제는 아니였던것 같다.
    
    P.S.
    코드가 정말 엉망진창인데 이는 두번이나 갈아엎어서 너무 귀찮은 내심정이 투과된것 같다.  
"""

N = int(sys.stdin.readline())
list_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
list_visit = [[0]*N for _ in range(N)]
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]
list_queue = deque()
info_baby = [] # x, y, now_size, eating_count
result = 0
break_token = 0
for y in range(N):
    for x in range(N):
        if list_map[y][x]==9:
            info_baby = [x, y, 2,0]
            list_map[y][x] = 0
            break_token = 1
            break
    if break_token:
        break

visit_count = 1
end = False
while not end:
    #print('===================', info_baby[2])
    #[print(a) for a in list_map]
    list_queue.append([info_baby[0], info_baby[1], 0])
    end = True
    list_food=[]
    while list_queue:
        now_x, now_y, count_dist = list_queue.popleft()
        for i in range(4):
            nx = dx[i] + now_x
            ny = dy[i] + now_y
            if 0 <= nx < N and 0 <= ny < N:
                if (list_map[ny][nx]==0 or list_map[ny][nx]==info_baby[2]) and list_visit[ny][nx] < visit_count:
                    if list_food:
                        if list_food[0][2] > count_dist:
                            list_queue.append([nx, ny, count_dist+1])
                            list_visit[ny][nx] = visit_count
                    else:
                        list_queue.append([nx, ny, count_dist+1])
                        list_visit[ny][nx] = visit_count
                elif 0<list_map[ny][nx]<info_baby[2] and list_visit[ny][nx] < visit_count:
                    if list_food:
                        if list_food[0][2] > count_dist:
                            list_food.append([nx, ny, count_dist+1])
                    else:
                        list_food.append([nx, ny, count_dist+1])
    if list_food:
        list_food.sort(key = lambda a:(a[1],a[0]))
        result += list_food[0][2]
        list_map[list_food[0][1]][list_food[0][0]] = 0
        info_baby[3]+=1
        
        if info_baby[2] == info_baby[3]:
            info_baby[2] += 1
            info_baby[3] = 0
        info_baby = [list_food[0][0], list_food[0][1], info_baby[2], info_baby[3]]
        end=False
    visit_count+=1
print(result)
