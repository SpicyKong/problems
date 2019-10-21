# https://www.acmicpc.net/problem/3190 문제 제목 : 뱀 , 언어 : Python, 날짜 : 2019-10-21, 결과 : 성공
# 1보다 큰 수는 뱀, 가장 큰 수는 머리
# 이동구현 : 방향+1위치 = 머리 + 1
#           그후 사과를 먹지 않았다면, 맵에 있는 수 중 만약 0보다 큰수는 모두 -1해줌
#           사과를 먹었다면, -1을 해주는 작업 X
# 근데 이거 파이썬3로 제출하면 틀리고, pypy3로 제출해야한다..
# 비효율적인가 보다


import sys

N = int(sys.stdin.readline())
list_map = [[0]*N for _ in range(N)]
list_apple = [list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]
action_range = int(sys.stdin.readline())
list_action = [sys.stdin.readline().split() for _ in range(action_range)]
for asdf in list_apple:
    list_map[asdf[0]-1][asdf[1]-1] = -1
end = False
direction = 0
time = 0
now_head =[0,0]
list_map[0][0]=1
action_num = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
while not end:
    
    #[print(a) for a in list_map]
    #print("======================")
    if 0 <= now_head[0] + dy[direction] < N and 0 <= now_head[1] + dx[direction] < N:
        
        if list_map[now_head[0] + dy[direction]][now_head[1]+ dx[direction]] == -1:
            pass
        elif list_map[now_head[0]+ dy[direction]][now_head[1]+ dx[direction]] > 0:
            end = True
        else:
            for y in range(N):
                for x in range(N):
                    if list_map[y][x] > 0:
                        list_map[y][x]-=1
        list_map[now_head[0]+ dy[direction]][now_head[1]+ dx[direction]] = list_map[now_head[0]][now_head[1]] + 1
        now_head[0]+= dy[direction]
        now_head[1]+= dx[direction]
    else:
        end = True
    time += 1
    if time == int(list_action[action_num][0]):
        if list_action[action_num][1] == 'D':
            direction+=1
        else:
            direction-=1
        if direction == -1:
            direction = 3
        if direction == 4:
            direction = 0
        if action_num +1 < action_range:
            action_num +=1
print(time)

"""

8
3
5 4
5 8
2 5
6
7 D
11 D
15 D
18 D
19 D
20 D

출처: https://stack07142.tistory.com/176 [Hello World]
"""
