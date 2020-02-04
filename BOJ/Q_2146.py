# https://www.acmicpc.net/problem/2146 문제 제목 : 다리 만들기 , 언어 : Python, 날짜 : 2020-02-04, 결과 : 성공
# DFS랑 BFS를 모두 사용해야하는 문제다
# 지금 보니 왜 DFS만 함수를 정의했는지 모르겠다ㅋㅋ
# 아 그리고 주석을 보면 알다시피 디버깅은 전부 프린트문으로 찍어가면서 한다..
# vscode로 디버깅툴 사용을 시도해봐도 왜인지 안된다..

import sys
from collections import deque
N = int(sys.stdin.readline())
list_map = [sys.stdin.readline().split() for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(list_map1, N, list_ocean):
    global dx, dy
    now = 1
    list_visit = [[0]*N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if list_map1[y][x] == '1':
                list_stack = [[x,y]]
                list_ocean.append(deque())
                list_map1[y][x] = now

                while list_stack:
                    now_x, now_y = list_stack.pop()
                    for i in range(4):
                        nx = dx[i] + now_x
                        ny = dy[i] + now_y
                        if 0 <= nx < N and 0 <= ny < N:
                            if list_map1[ny][nx] == '1':# and not list_visit[ny][nx]:
                                list_stack.append([nx,ny])
                                list_map1[ny][nx] = now
                            elif (list_map1[ny][nx] == '0' or list_map1[ny][nx] == 0) and not list_visit[now_y][now_x]:
                                list_ocean[now-1].append([now_x, now_y])
                                list_visit[now_y][now_x] = 1
                now+=1
            elif list_map1[y][x] == '0':
                list_map1[y][x] = 0


result = 10005
list_oceans = []
dfs(list_map, N, list_oceans)

list_save = [a[:] for a in list_map]
for now, oceans in enumerate(list_oceans):
    now += 1
    list_count = [len(oceans)]
    now_count = 0
    distance = 0
    #print("#######################")
    #[print(a) for a in list_save]
    #print(result)
    while oceans:
        x, y = oceans.popleft()
        list_count[-1] -= 1
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0 <= nx < N and 0 <= ny < N:
                if list_save[ny][nx] <= 0 and not list_save[ny][nx] == now * -1:
                    list_save[ny][nx] = now * -1
                    oceans.append([nx, ny])
                    now_count += 1
                elif list_save[ny][nx] > 0 and not list_save[ny][nx] == now:
                    if result > distance:
                        result = distance
                    #print(distance, list_save[ny][nx])
                    ocaens = []
                    break
        if not list_count[-1]:
            list_count.append(now_count)
            distance += 1
            now_count = 0
                    

#[print(a) for a in list_save]
print(result)
#[print(a) for a in list_map]
#print("asdlhdjksahj")
#[print(a) for a in list_save]
#print(list_oceans)

"""
10
1 1 1 0 0 0 0 0 1 1
1 1 1 1 0 0 0 0 1 1
1 0 1 1 0 0 0 0 1 1
0 0 1 1 1 0 0 0 0 1
0 0 0 1 0 0 1 0 0 1
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0



"""
