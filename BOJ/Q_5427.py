# https://www.acmicpc.net/problem/5427 문제 제목 : 불 , 언어 : Python, 날짜 : 2020-04-29, 결과 : 성공
"""
    이 문제는 흔한 유형의 BFS문제다. 불을 키우는 조건이 맞는 지 확인하고 플레이어가 다음번 턴에 갈 수 있는곳을 모두 방문하면 된다.

    과제가 많아서 양심에 찔리지만 비교적 쉬운 BFS문제를 풀었다.. 하지만 과제가 중간고사를 대체하는것이라 열심히 해야하기 때문에 어쩔수 없었다..
    그리고 오늘 운좋게 소마 2차 온라인 코테 합격메일이 왔다. 문제는 내 스펙이 전혀 없기때문에 붙을 가능성은 희박할거 같다. 하지만 그래도
    다음번 지원을 위해 면접을 한번 경험해 보는것은 추후에 분명히 도움이 되리라 생각하고 열심히 준비 해야 겠다.
"""

import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def fire(imsi_queue):
    result_queue = deque()
    while imsi_queue:
        now_x, now_y = imsi_queue.popleft()
        for i in range(4):
            nx = dx[i] + now_x
            ny = dy[i] + now_y
            if 0 <= nx < N and 0 <= ny < M:
                if not list_visit[ny][nx] or list_visit[ny][nx]==1:
                    list_visit[ny][nx] = 2
                    result_queue.append([nx, ny])
    return result_queue

def bfs():
    global N, M, list_map, list_visit
    list_queue = deque()
    list_fire = deque()
    for y in range(M):
        for x in range(N):
            if list_map[y][x] == '*':
                list_fire.append([x, y])
                list_visit[y][x] = 2
            elif list_map[y][x] == '@':
                list_queue.append([x, y, 0])
                list_visit[y][x] = 1
            elif list_map[y][x] == '#':
                list_visit[y][x] = 3
    count_queue = 1
    next_queue = 0
    while list_queue:
        now_x, now_y, now_count = list_queue.popleft()
        count_queue -= 1
        if 0 >= count_queue:
            list_fire = fire(list_fire)
            count_queue = next_queue
            next_queue = 0
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not list_visit[ny][nx]:
                    list_visit[ny][nx] = 1
                    list_queue.append([nx, ny, now_count+1])
                    next_queue+=1
            else:
                return now_count+1

    return 'IMPOSSIBLE'
T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    list_map = [sys.stdin.readline().strip() for _ in range(M)]
    list_visit = [[0]*N for _ in range(M)]
    print(bfs())
