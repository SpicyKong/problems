# https://www.acmicpc.net/problem/2636 문제 제목 : 치즈 , 언어 : Python, 날짜 : 2020-03-15, 결과 : 성공
"""
    회고:
    먼저 맵의 외곽은 항상 0임이 보장되므로 시작전에 (0,0)에서 BFS를 해줘 외부공기를 체크해준다.
    이때 치즈의 위치는 큐에 따로 저장한다. 그후 치즈의 위치가 저장된 큐를 pop해주며 만약 그 치즈가 외부공기와 접촉해있다면
    녹아없어질 치즈들을 저장하는 새로운 리스트에 저장한다. 만약 외부공기와 접촉하지 않았다면 다시 치즈의 위치를 저장해 두었던 큐에 push해준다.
    
    사실 이문제와 이름이 같은 2638_치즈 문제를 풀려고 했지만 계속 시간초과가 나서
    그냥 이 문제에 맞는 코드로 수정했다ㅠㅠ 한번 2638번 문제도 풀어보도록 해야겠다.
"""

import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
N, M = map(int, sys.stdin.readline().split())
list_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
list_visit = [[0]*M for _ in range(N)]
def confirm_air(x,y):
    list_queue = deque()
    list_queue.append([x,y])
    while list_queue:
        now_x, now_y = list_queue.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if not list_map[ny][nx] and not list_visit[ny][nx]:
                    list_visit[ny][nx] = -1
                    list_queue.append([nx, ny])

list_visit [0][0]=-1
confirm_air(0,0)
list_cheese = deque()
count_cheese = 0
for y in range(N):
    for x in range(M):
        if list_map[y][x]:
            list_cheese.append([x,y])
            count_cheese+=1
time = 0
num_of_cheese = count_cheese
melting_list = []
count_cheese1 = 0
while list_cheese:
    cx, cy = list_cheese.popleft() # Cheese X, Cheese Y
    count_cheese-=1
    count_air_side = 0
    for i in range(4):
        if not list_map[cy + dy[i]][cx + dx[i]] and list_visit[cy + dy[i]][cx + dx[i]] == -1:
            count_air_side=1
            break
    if count_air_side:
        melting_list.append([cx, cy])
    else:
        list_cheese.append([cx, cy])
        count_cheese1 += 1
        
    if count_cheese==0:
        if count_cheese1:
            num_of_cheese = count_cheese1
        while melting_list:
            ix, iy = melting_list.pop() # ImsiX, ImsiY
            list_map[iy][ix] = 0
            list_visit[iy][ix] = -1
            for i in range(4):
                if not list_map[iy + dy[i]][ix + dx[i]] and not list_visit[iy + dy[i]][ix + dx[i]]:
                    #print("asdhjksdahjkasdhjkdas")
                    confirm_air(ix + dx[i], iy + dy[i])
        count_cheese = count_cheese1
        count_cheese1 = 0
        time += 1
print(time)
print(num_of_cheese)
