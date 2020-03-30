# https://www.acmicpc.net/problem/2239 문제 제목 : 스도쿠 , 언어 : Python, 날짜 : 2020-03-30, 결과 : 성공
"""
    회고:
    무난했다. 하지만 중간에 변수명을 햇갈린게 너무 많아서 삽질좀 했다..ㅠㅠ
    백트레킹에 대해서 조금씩 알아가는 중인데 백트레킹 신기한거같다.
    저번에는 풀이를 보고 공부해볼 엄두도 못내고 다른문제를 풀러갔던 기억이 있는데
    그래도 이제는 풀이를 안보고 풀었으니 성장한것같다ㅋㅋ
"""

import sys
from collections import deque
sys.setrecursionlimit(10**6)
def where(x,y):
    if 0 <= y <3 and 0 <= x <3:
        return [0,0]
    elif 0 <= y < 3 and 3 <= x < 6:
        return [3,0]
    elif 0 <= y < 3 and 6 <= x:
        return [6,0]
    elif 3 <= y < 6 and 0 <= x < 3:
        return [0,3]
    elif 3 <= y < 6 and 3 <= x < 6:
        return [3,3]
    elif 3 <= y < 6 and 6 <= x:
        return [6,3]
    elif 6 <= y and 0 <= x < 3:
        return [0,6]
    elif 6 <= y and 3 <= x < 6:
        return [3,6]
    elif 6 <= y and 6 <= x:
        return [6,6]

def sdoku(i):
    global list_blank, list_map, count, end
    if i >= count:
        if not end:
            [print(*a) for a in list_map]
            end = 1
        return
    if end:
        return
    now_x = list_blank[i][0]
    now_y = list_blank[i][1]
    now_can = [1]*10
    for y in range(3):
        for x in range(3):
            now_can[list_map[y + list_blank[i][2][1]][x + list_blank[i][2][0]]] = 0

    for x in range(9):
        now_can[list_map[now_y][x]] = 0
    for y in range(9):
        now_can[list_map[y][now_x]] = 0
    token = 0
    for j in range(1,10):
        if now_can[j]:
            token = 1
            list_map[now_y][now_x] = j
            sdoku(i+1)
            list_map[now_y][now_x] = 0
    
    if not token:
        return


list_map = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]
list_blank = deque()
count = 0
end = 0
for y in range(9):
    for x in range(9):
        if list_map[y][x] == 0:
            list_blank.append([x,y,where(x,y)])
            count += 1
sdoku(0)
"""
0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0
"""
