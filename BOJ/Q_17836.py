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
