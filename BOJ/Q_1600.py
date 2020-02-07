# https://www.acmicpc.net/problem/1600 문제 제목 : 말이 되고픈 원숭이 , 언어 : Python, 날짜 : 2020-02-07, 결과 : 실패
# 시간초과 + 메모리 초과..
import sys
from collections import deque

K = int(sys.stdin.readline())
W, H = map(int, sys.stdin.readline().split())

list_map = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
list_visit = [[0]*W for _ in range(H)]

list_visit[0][0] = [0,K]
list_queue = deque()
list_queue.append([0,0])
dx = [1, -1, 0, 0, 1, 2, 2, 1, -1, -2, -2, -1]
dy = [0, 0, 1, -1, 2, 1, -1, -2, -2, -1, 1, 2]



while list_queue:
    #print("======================")
    #[print(a) for a in list_visit]
    now_x, now_y = list_queue.popleft()
    if now_x == W -1 and now_y == H -1:
        #print("End !")
        break
    if list_visit[now_y][now_x][1]:
        knight = 8
    else:
        knight = 0
    for i in range(4 + knight):
        nx = dx[i] + now_x
        ny = dy[i] + now_y
        if 0 <= nx < W and 0 <= ny < H:
            if (not list_visit[ny][nx] or (list_visit[now_y][now_x][0] + 1 >= list_visit[ny][nx][0] and list_visit[now_y][now_x][1] > list_visit[ny][nx][1]))and not list_map[ny][nx]:
                if i > 3:
                    list_visit[ny][nx] = [list_visit[now_y][now_x][0] + 1, list_visit[now_y][now_x][1] - 1]
                else:
                    list_visit[ny][nx] = [list_visit[now_y][now_x][0] + 1, list_visit[now_y][now_x][1]]
                list_queue.append([nx, ny])
            #if ny == H -1 and nx == W - 1:
                #print(list_visit[ny][nx])
#[print(a) for a in list_visit]
if list_visit[H-1][W-1]:
    print(list_visit[H-1][W-1][0])
else:
    print(-1)

"""
3
4 5
0 1 1 1
1 1 0 1
1 1 1 1
1 1 1 0
1 1 1 0

1
5 5
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 1 1
0 0 0 1 0
"""
