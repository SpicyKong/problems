# https://www.acmicpc.net/problem/1938 문제 제목 : 통나무 옮기기 , 언어 : Python, 날짜 : 2020-05-24, 결과 : 실패

# https://www.acmicpc.net/problem/1938 문제 제목 : 통나무 옮기기 , 언어 : Python, 날짜 : 2020-05-25, 결과 : 성공
"""
    회고:
    지금보니깐 전에 코드를 어제 안올렸었다. 일단 이 문제를 굉장히 복잡하게 풀었는데, 내가 푼 방식은 이렇다.
    1. 시작점을 찾는다 가장 먼저 탐색되는 B칸의 주변 1칸을 모두 탐색하면 나오는 B칸이 중앙(시작점)이다.
    2. 양 끝점을 고려하면서 탐색을 한다. (상 하 좌 우)
    3. 턴을 할 수 있으면 턴도 한다.
    위의 과정을 반복하면 된다.
"""
import sys
from collections import deque

def canIturn(x, y):
    global dx, dy, d, check, N
    for i in (0, 1, 2, 3, 4, 5, 6, 7):
        nx = x + check[i][0]
        ny = y + check[i][1]
        if 0<=nx<N and 0<=ny<N and not list_map[ny][nx] == '1':
            pass
        else:
            return False
    return True

def solve():
    global dx, dy, d, check, N, list_map
    N = int(sys.stdin.readline())
    list_map = [list(sys.stdin.readline().strip()) for _ in range(N)]
    list_visit = [[[0,0,0,0] for _ in range(N)] for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    ddx = ((0,0), (1, -1), (1, -1), (1, -1))
    ddy = ((1,-1), (-1,1), (0,0), (1, -1))
    check = ((1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1))
    list_queue = deque()
    to = 0
    for y in range(N):
        for x in range(N):
            if to:
                break
            if list_map[y][x]=='B':
                for i,c in enumerate(((0,1), (-1,1), (1, 0), (1,1))):
                    nx = x+ c[0]
                    ny = y + c[1]
                    if 0<=nx<N and 0<=ny<N and list_map[ny][nx]=='B':
                        list_queue.append((nx, ny, 1, i))
                        list_visit[ny][nx][i] = 1
                        to = 1
                        break
        if to:
            break
    #[print(a) for a in list_map]
    #print(list_queue)
    while list_queue:
        #[print(a) for a in list_visit]
        #print()
        now_x, now_y, now_count, now_d = list_queue.popleft()
        for i in (0,1,2,3):
            nx = dx[i] + now_x
            ny = dy[i] + now_y
            #for j in (0,1,2,3):
            x1=nx+ddx[now_d][0]
            x2=nx+ddx[now_d][1]
            y1=ny+ddy[now_d][0]
            y2=ny+ddy[now_d][1]
            if 0<=x1<N and 0<=y1<N and 0<=x2<N and 0<=y2<N:
                if list_visit[ny][nx][now_d]:
                    continue
                if list_map[y1][x1] =='1' or list_map[y2][x2] == '1' or list_map[ny][nx] =='1':
                    continue
                elif list_map[y1][x1] =='E' and list_map[y2][x2] == 'E':
                    return now_count
                list_visit[ny][nx][now_d] = now_count+1
                list_queue.append((nx, ny, now_count+1, now_d))
        if canIturn(now_x, now_y):
            if not list_visit[now_y][now_x][(now_d+2)%4]:
                x1=now_x+ddx[(now_d+2)%4][0]
                x2=now_x+ddx[(now_d+2)%4][1]
                y1=now_y+ddy[(now_d+2)%4][0]
                y2=now_y+ddy[(now_d+2)%4][1]
                if list_map[y1][x1] =='E' and list_map[y2][x2] == 'E' and list_map[now_y][now_x] =='E':
                    return now_count
                list_queue.append((now_x, now_y, now_count+1, (now_d+2)%4))
                list_visit[now_y][now_x][(now_d+2)%4] = now_count+1
    return 0

print(solve())
#[print(a) for a in list_visit]
"""
B0011111
B0000EEE
B0011111
11111111
11111111
11111111
11111111
11111111
4
00BE
0B0E
B00E
0000

4
0B00
EB00
EB00
E000

4
BBB0
0E00
0E00
0E00

B001100E
B000000E
B001100E
11111111
11111111
11111111
11111111
11111111


"""
