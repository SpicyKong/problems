# https://www.acmicpc.net/problem/2580 문제 제목 : 스도쿠 , 언어 : Python, 날짜 : 2019-09-28, 결과 : 실패
# 맨 처음에는 간단히 생각해서 이런식으로 구현을 했는데
"""
아래와 같은 상황에서는 무한루프에 빠지게 된다.
0 0 5 4 6 9 2 7 8
0 0 2 1 3 5 6 4 9
4 6 9 2 7 8 1 3 5
3 2 1 5 4 6 8 9 7
8 7 4 9 1 3 5 2 6
5 9 6 8 2 7 4 1 3
9 1 7 6 5 2 3 8 4
6 4 3 7 8 1 9 5 2
2 5 8 3 9 4 7 6 1

다음번 시도에서는 각 파트별(가로, 세로, 3x3)에서 얻은 정보를 취합해 결정하는 방식을 추가해야 겠다.
추가로 '백트래킹'을 공부해야겠다.
"""


import sys
from collections import deque
list_map = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
list_queue = deque()
list_zero = []
for y in range(9):
    for x in range(9):
        if list_map[y][x] == 0:
            list_queue.append([x,y])
            list_zero.append(0)
asdf = 0
while list_queue:
    x, y = list_queue.popleft()
    onetonine = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    count = 0
    b_add = 0
    if b_add == 0:
        for ax in range(9):
            if list_map[y][ax]:
                onetonine[list_map[y][ax]-1] = 1
                count += 1
        if count == 8:
            list_map[y][x] = [i+1 for i in range(9) if onetonine[i] == 0][0]
            b_add = 1
            
    onetonine = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    count = 0
    if b_add == 0:
        for ay in range(9):
            if list_map[ay][x]:
                onetonine[list_map[ay][x]-1] = 1
                count += 1
        if count == 8:
            list_map[y][x] = [i+1 for i in range(9) if onetonine[i] == 0][0]
            b_add = 1
    onetonine = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    count = 0
    if b_add == 0:
        part_x = 0
        part_y = 0
        if 0 <= x < 3:
            part_x = 0
        elif 3 <= x < 6:
            part_x = 3
        else:
            part_x = 6
        if 0 <= y < 3:
            part_y = 0
        elif 3 <= y < 6:
            part_y = 3
        else:
            part_y = 6
        for by in range(3):
            for bx in range(3):
                if list_map[by + part_y][bx + part_x]:
                    onetonine[list_map[by + part_y][bx + part_x]-1] = 1
                    count+=1
        if count == 8:
            list_map[y][x] = [i+1 for i in range(9) if onetonine[i] == 0][0]
            b_add = 1
    if b_add == 0:
        list_queue.append([x,y])
[print(" ".join([str(b) for b in a])) for a in list_map]
"""

0 0 5 4 6 9 2 7 8
0 0 2 1 3 5 6 4 9
4 6 9 2 7 8 1 3 5
3 2 1 5 4 6 8 9 7
8 7 4 9 1 3 5 2 6
5 9 6 8 2 7 4 1 3
9 1 7 6 5 2 3 8 4
6 4 3 7 8 1 9 5 2
2 5 8 3 9 4 7 6 1

"""
