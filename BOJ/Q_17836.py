# https://www.acmicpc.net/problem/17836 문제 제목 : 공주님을 구해라! , 언어 : Python, 날짜 : 2019-11-10, 결과 : 실패
# 왜 틀리는 걸까?

import sys
from collections import deque


N, M, T = map(int, sys.stdin.readline().split())
list_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
list_visit = [[0]*M for _ in range(N)]
list_visit[0][0] = 1
list_queue1 = deque([[0,0]])
list_queue2 = deque()
time = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

a, b = 0, 0
sword = []
time_sword = 0
sword_b = 0
end = 0

while list_queue1 or list_queue2:
    while list_queue1:
        x, y = list_queue1.popleft()
        if list_map[y][x] == 2 and not time_sword:
            sword = [x,y]
            time_sword = time
            sword_b = 1
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0 <= ax < M and 0 <= ay < N:
                if not list_map[ay][ax] == 1 and not list_visit[ay][ax]:
                    list_queue2.append([ax, ay])
                    list_visit[ay][ax] = 1
                    if ay == N-1 and ax == M-1:
                        end = time+1
                    a=1
                
                
    if a:
        time += 1
        a = 0
    
    while list_queue2:
        x, y = list_queue2.popleft()
        if list_map[y][x] == 2 and not time_sword:
            sword = [x,y]
            time_sword = time
            sword_b = 1
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0 <= ax < M and 0 <= ay < N:
                if not list_map[ay][ax] == 1 and not list_visit[ay][ax]:
                    list_queue1.append([ax, ay])
                    list_visit[ay][ax] = 1
                    b = 1
                    if ay == N-1 and ax == M-1:
                        end = time+1
                
                #print("[][][][]][][][]]]]][")
    if b:
        time += 1
        b = 0

if end == 0 and sword_b == 0:
    print("Fail")
elif end > 0 and sword_b == 0:
    if end <= T:
        print(end)
    else:
        print("Fail")
elif end == 0 and sword_b == 1:
    time_sword = (M -1) - sword[0] + (N-1) - sword[1] + time_sword
    if time_sword <= T:
        print(time_sword)
    else:
        print("Fail")
else:
    if end <= T or sword_b <= T:
        time_sword = (M -1) - sword[0] + (N-1) - sword[1] + time_sword
        if end <= time_sword:
            print(end)
        elif end > time_sword:
            print(time_sword)

#print(end, sword_b)
#if end == 0 and sword_b == 0:
#    print('Fail')

#time_sword = (M -1) - sword[0] + (N-1) - sword[1] + time_sword
#print(sword, time_sword)



#print(time)

# [print(a) for a in list_visit]

"""
time_sword = (M -1) - sword[0] + (N-1) - sword[1] + time_sword
    if time_sword > T and time > T:
        print("Fail")
    elif time_sword > time:
        print(time)
    elif time_sword < time:
        print(time_sword)
2 2 1
0 2
0 0

5 6 100
0 0 0 0 1 2
1 1 1 0 1 1
0 0 0 0 1 0
0 1 1 1 1 0
0 0 0 0 0 0

5 6 100
0 0 0 0 0 2
1 1 1 1 1 1
0 0 0 0 1 0
0 1 1 1 1 0
0 0 0 0 0 0

5 6 100
2 0 0 0 0 0
1 1 1 1 1 1
0 0 0 0 1 1
0 1 1 1 1 1
1 1 1 1 1 0

5 6 100
0 0 0 0 1 2
1 1 1 0 1 1
0 0 0 0 1 1
0 1 1 0 1 1
1 1 1 0 0 0
"""
###########################################################################################
# https://www.acmicpc.net/problem/17836 문제 제목 : 공주님을 구해라! , 언어 : Python, 날짜 : 2020-03-02, 결과 : 성공
"""
    회고:
    요즘 문제고르기가 너무 오래걸려서 예전에 시도했지만 틀린문제들을 다시 풀어보는중이다.
    내가 예전에 처음 시도 했던 방법은 그람을 찾으면 그람의 좌표와 목적지의 좌표를 맨해튼 거리로 구해준뒤
    정상적으로 도착한 시간과 비교해 더 작은것을 최소거리로 사용하는 것이였다. 하지만 아쉽게도 계속 틀렸었다.

    이 문제는 '그람'을 찾으면 그냥 오른쪽과 아래쪽으로 탐색해 나가는 부분만 추가해주면 된다.
    그리고 예전에 한번만 벽을 뚫을수있었던 문제처럼 그람을 가지고 있는지에 대한 정보또한 계속 넘겨주면 된다.

"""
import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
N, M, T = map(int, sys.stdin.readline().split())
list_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
list_visit = [[[0,0] for _ in range(M)] for _ in range(N)] # check, count
list_queue = deque([[0,0,0,1]])
list_visit[0][0]= [1,1]
while list_queue:
    now_x, now_y, gram, count = list_queue.popleft()
    for i in range(4):
        nx = dx[i] + now_x
        ny = dy[i] + now_y
        if 0 <= nx < M and 0 <= ny < N:
            if gram:
                if i == 0 or i == 2:
                    if not list_visit[ny][nx][0] or list_visit[ny][nx][0] == 1:
                        list_visit[ny][nx][0] = 2
                        list_visit[ny][nx][1] = count
                        list_queue.append([nx, ny, 1, count+1])
            else:
                if not list_map[ny][nx] and not list_visit[ny][nx][0]:
                    list_visit[ny][nx][0] = 1
                    list_visit[ny][nx][1] = count
                    list_queue.append([nx, ny, 0, count+1])
                elif list_map[ny][nx] == 2 and not list_visit[ny][nx][0]:
                    list_visit[ny][nx][0] = 2
                    list_visit[ny][nx][1] = count+1
                    list_queue.append([nx, ny, 1, count+1])
            if ny == N - 1 and nx == M - 1:
                list_queue = []
#[print(a) for a in list_visit]
if not list_visit[N-1][M-1][1]:
    print('Fail')
elif list_visit[N-1][M-1][1] <= T:
    print(list_visit[N-1][M-1][1])
else:
    print('Fail')
"""
6 6 10
0 0 0 0 1 1
0 0 0 0 0 2
1 1 1 0 1 0
0 0 0 0 0 0
0 1 1 1 1 1
0 0 0 0 0 0
"""
