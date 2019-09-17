# https://www.acmicpc.net/problem/2667 문제 제목 : 단지번호붙이기 , 언어 : Python, 날짜 : 2019-09-17, 결과 : 성공

import sys
from collections import deque

def quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    lesser, aver, greater = [], [], []
    for element in arr:
        if element > pivot:
            greater.append(element)
        elif element < pivot:
            lesser.append(element)
        else:
            aver.append(element)
    return quick(lesser) + aver + quick(greater)

N = int(sys.stdin.readline())
list_map = [list(map(int, list(sys.stdin.readline()[:-1]))) for _ in range(N)]
list_visit = [[0]*N for _ in range(N)]
list_queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
count_result = 0
list_count_dong = []
for y in range(N):
    for x in range(N):
        if list_map[y][x]:
            list_queue.append([x,y])
            count_dong = 1
            while list_queue:
                tx, ty = list_queue.popleft()
                list_map[ty][tx] = 0
                for i in range(4):
                    ax = tx + dx[i]
                    ay = ty + dy[i]
                    if 0 <= ax < N and 0 <= ay < N:
                        if list_map[ay][ax]==1 and list_visit[ay][ax] == 0:
                            list_visit[ay][ax] = 1
                            list_queue.append([ax, ay])
                            count_dong+=1
            list_count_dong.append(count_dong)
            count_result+=1
print(count_result)
[print(a) for a in quick(list_count_dong)]
