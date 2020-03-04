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
########################################################################################
# https://www.acmicpc.net/problem/1600 문제 제목 : 말이 되고픈 원숭이 , 언어 : Python, 날짜 : 2020-03-04, 결과 : 성공
"""
    회고:
    이 문제를 풀기전에 벽 부수고 이동하기라는 문제를 미리 풀어 보았다면 정말 도움이 될것같다.
    내가 푼방식은 이렇다.
    1) 먼저 큐에 저장되는 자료의 형태는 [x좌표, y좌표, 점프가능 횟수, 현재까지 이동 카운트] 
    2) 기본 이동을 나타내는 dy, dx를 이용해 움직임.
    3) 점프가능 횟수가 남아있다면, hy, hx를 이용해 추가로 움직임
    4) 추가로 만약에 이동하려는 칸이 방문했던 칸이지만 미리 점프를써서 이동한칸이라면 방문을 할수있게 해야함.
        왜냐하면 점프를 아껴야 도착할수있는 상황도 있을수도 있기때문이다.
    
"""
import sys
from collections import deque

horse = int(sys.stdin.readline())
W, H = map(int, sys.stdin.readline().split())
list_map = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
list_visit = [[-1]*W for _ in range(H)]
list_queue = deque()
list_queue.append([0,0,horse,0]) #x, y, horse, count
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
hx = [1, 2, 2, 1, -1, -2, -2, -1]
hy = [2, 1, -1, -2, -2, -1, 1, 2]
result = -1
while list_queue:
    now_x, now_y, now_horse, count = list_queue.popleft()
    if now_y == H-1 and now_x == W-1:
        result = count
        break
    for i in range(4):
        nx = dx[i] + now_x
        ny = dy[i] + now_y
        if 0 <= nx < W and 0 <= ny < H:
            if not list_map[ny][nx] and (list_visit[ny][nx] == -1 or list_visit[ny][nx] < now_horse):
                list_queue.append([nx,ny,now_horse,count+1])
                list_visit[ny][nx] = now_horse
    if now_horse>0:
        for i in range(8):
            nx = hx[i] + now_x
            ny = hy[i] + now_y
            if 0 <= nx < W and 0 <= ny < H:
                if not list_map[ny][nx] and (list_visit[ny][nx] == -1 or list_visit[ny][nx] < now_horse-1):
                    list_queue.append([nx, ny, now_horse - 1, count+1])
                    list_visit[ny][nx] = now_horse-1

print(result)

