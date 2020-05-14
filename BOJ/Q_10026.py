# https://www.acmicpc.net/problem/10026 문제 제목 : 적록색약 , 언어 : Python, 날짜 : 2020-05-14, 결과 : 성공 
"""
    회고:
    그냥 BFS를 돌면서 구역을 구분해 주는 문제인데, 색약인 사람이 봤을때 R과 G가 구분이 안되므로 R과 G 모두 R로 취급해 주었다.
"""
import sys
from collections import deque

def findC(mode):
    global N, list_map
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    list_color = [{'R':'R', 'G':'G', 'B':'B'}, {'R':'R', 'G':'R', 'B':'B'}]
    list_visit = [[0]*N for _ in range(N)]
    list_queue = deque()
    count = 0
    for y in range(N):
        for x in range(N):
            if not list_visit[y][x]:
                list_visit[y][x] = 1
                list_queue.append((x,y))
                while list_queue:
                    now_x, now_y = list_queue.popleft()
                    for i in range(4):
                        nx = dx[i] + now_x
                        ny = dy[i] + now_y
                        if 0 <= nx < N and 0 <= ny < N:
                            if list_color[mode][list_map[now_y][now_x]] == list_color[mode][list_map[ny][nx]] and not list_visit[ny][nx]:
                                list_visit[ny][nx] = 1
                                list_queue.append((nx, ny))
                count+=1
    return count


N = int(sys.stdin.readline())
list_map = [list(sys.stdin.readline().strip()) for _ in range(N)]
print(findC(0), findC(1))
