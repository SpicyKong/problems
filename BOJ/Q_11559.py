# https://www.acmicpc.net/problem/11559 문제 제목 : Puyo Puyo , 언어 : Python, 날짜 : 2019-09-22, 결과 : 실패
# 런타임 에러..ㅠ 내일 다시 보기로..
# 여러 예제들은 올바르게 나오는데..

import sys
from collections import deque
list_map = [list(sys.stdin.readline()[:-1]) for _ in range(12)]

def gravity():
    global list_map
    for i in range(6):
        count_down_block = 0
        for y in range(12):
            if not list_map[11-y][i] == '.':
                if not count_down_block == y:
                    save = list_map[11-y][i]
                    list_map[11-y][i] = '.'
                    list_map[11-count_down_block][i] = save
                count_down_block+=1
def explode():
    global list_map
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    list_queue = deque()
    list_visit = [[0]*6 for _ in range(12)]
    count_explode = 0
    for y in range(12):
        for x in range(6):
            if not list_map[y][x] == '.' and list_visit[y][x] == 0:
                save_color = list_map[y][x]
                list_queue.append([x, y])
                list_explode = deque()
                list_explode.append([x, y])
                list_visit[y][x] = 1
                count_block = 1
                while list_queue:
                    tx, ty = list_queue.popleft()
                    for i in range(4):
                        ax = tx + dx[i]
                        ay = ty + dy[i]
                        if 0 <= ax < 6 and 0 <= ay < 12:
                            if list_map[ay][ax] == save_color and list_visit[ay][ax] == 0:
                                list_visit[ay][ax] = 1
                                list_queue.append([ax, ay])
                                list_explode.append([ax, ay])
                                count_block+=1
                if count_block >= 4:
                    for bx, by in list_explode:
                        list_map[by][bx] = '.'
                    count_explode+=1
    if count_explode > 0:
        return 1
    else:
        return 0
end = False
count = 0
while not end:
    num = explode()
    count += num
    if num == 0:
        end = True
    else:
        gravity()
        #print("========================")
        #[print(a) for a in list_map]
print(count)

# to do : Making a explode function (using breadth first search)

"""

......
.RRYGG
.RRYGG
.RRYGG
.RRYGG
RRYGGl
RRYGGl
RRYGGl
RRYGGl
lYGlll
RRYGll
RRYGGl

"""
