# https://www.acmicpc.net/problem/7562 문제 제목 : 나이트의 이동 , 언어 : Python, 날짜 : 2019-10-05, 결과 : 성공
#오랜만에 BFS복습 할 겸 풀었는데 몇일 안했다고 까먹었나보다.. 짜는데 머리가 안돌아가는게 느껴진다..


import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    I = int(sys.stdin.readline())
    list_now = list(map(int, sys.stdin.readline().split()))
    list_goal = list(map(int, sys.stdin.readline().split()))
    list_map = [[0]*I for _ in range(I)]
    list_visit = [[0]*I for _ in range(I)]
    list_map[list_now[1]][list_now[0]] = 1
    list_map[list_goal[1]][list_goal[0]] = 2
    list_queue1 = deque()
    list_queue2 = deque()
    list_queue1.append(list_now)
    end = False
    count = 0
    c=0
    while not end:
        while list_queue1:
            if c==0:
                count+=1
                c+=1
            tx, ty = list_queue1.popleft()
            if tx == list_goal[0] and ty == list_goal[1]:
                list_queue1=[]
                list_queue2=[]
                end = True
                break
            dx = [1, 2, 2, 1, -1, -2, -2, -1]
            dy = [2, 1, -1, -2, -2, -1, 1, 2]
            for i in range(8):
                ax = tx + dx[i]
                ay = ty + dy[i]
                if 0 <= ax < I and 0 <= ay < I:
                    if not list_map[ay][ax] == 1 and list_visit[ay][ax] == 0:
                        list_visit[ay][ax] = 1
                        list_queue2.append([ax,ay])
        c=0
        while list_queue2:
            if c==0:
                count+=1
                c+=1
            tx, ty = list_queue2.popleft()
            if tx == list_goal[0] and ty == list_goal[1]:
                list_queue1=[]
                list_queue2=[]
                end = True
                break
            dx = [1, 2, 2, 1, -1, -2, -2, -1]
            dy = [2, 1, -1, -2, -2, -1, 1, 2]
            for i in range(8):
                ax = tx + dx[i]
                ay = ty + dy[i]
                if 0 <= ax < I and 0 <= ay < I:
                    if not list_map[ay][ax] == 1 and list_visit[ay][ax] == 0:
                        list_visit[ay][ax] = 1
                        list_queue1.append([ax,ay])
        c=0
    print(count-1)
