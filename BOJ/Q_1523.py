# https://www.acmicpc.net/problem/1525 문제 제목 : 퍼즐 , 언어 : Python, 날짜 : 2020-04-28, 결과 : 성공
"""
    회고:
    엄청난 사실을 알았다. 회고에서 오타가 나면 최고가 된다.
    방문 체크 하는 방법이 까다로울거 같아서 리스트를 튜플로 바꾼뒤 set에다가 집어넣어 방문체크를 했다.
    메모리 초과가 날 줄 알았는데 다행히 메모리 초과는 나지 않았다. 근데 솔직히 여기서 BFS라고 써져 있어서 풀었지
    만약 코드포스나 코테같은곳에서 만났다면 못 풀었을거 같다. 문제를 보고 솔루션을 떠올릴수 있는 경지에 이르고 싶다.
"""

import sys
from collections import deque

def sawp(list_a, a, b):
    list_b = list_a[:]
    s = list_b[a]
    list_b[a] = list_b[b]
    list_b[b] = s
    return list_b

def solve():
    list_map1 = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
    list_map = []
    set_visit = set()
    for y in range(3):
        for x in range(3):
            list_map.append(list_map1[y][x])
            if not list_map1[y][x]:
                where_zero = y*3+x
    dx = [1, -1, 0, 0]
    dy = [0, 0, 3, -3]
    goal = (1,2,3,4,5,6,7,8,0)
    if tuple(list_map) == goal:
        return 0
    list_queue = deque()
    list_queue.append([list_map,where_zero,0])
    while list_queue:
        #print(list_queue)
        now_map, where_zero, now_count = list_queue.popleft()
        #print(now_map)
        for i in range(4):
            nx = where_zero + dx[i]
            ny = where_zero + dy[i]
            if (i<=1 and nx//3 == where_zero//3) or (i>=2 and 0 <= ny <= 8):
                if i <= 1:
                    next_zero = nx
                else:
                    next_zero = ny
                save_list = sawp(now_map, where_zero, next_zero)
                #print(save_list)
                save_tuple = tuple(save_list)
                if not save_tuple in set_visit:
                    list_queue.append([save_list, next_zero, now_count+1])
                    set_visit.add(save_tuple)
                if save_tuple == goal:
                    return now_count + 1
    return -1
print(solve())

