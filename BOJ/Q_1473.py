# https://www.acmicpc.net/problem/1473 문제 제목 : 미로 탈출 , 언어 : Python, 날짜 : 2020-03-21, 결과 : 실패
import sys
from collections import deque
"""
    생각한 방법:
    1. 문과 문 사이의 이동가능하다면 계속 BFS를 해준다.
    2. 만약 이동이 불가능 하다면 문을 돌리면 이동할수있는지 확인하고 가능하면 result+2한값을 큐에 넣어준다.
    라고 생각하면 될줄알았는데 생각해보니 버튼을 작동시키면 해당 열과 행의 문이 모두 돌아간다.
    이 부분이 까다로운것 같다. 다시풀어봐야겠다.

"""
"""
A 아래 위 오른 왼
B 
C 위 아래
D 왼 오른

"""
dict_door = {'A':[0,1,2,3], 'B':[], 'C':[2,3], 'D':[0,1]}
turn_door = {'A':[0,1,2,3], 'B':[], 'C':[0,1], 'D':[2,3]}
list_door = [dict_door, turn_door]
N, M = map(int, sys.stdin.readline().split())
list_map = [list(sys.stdin.readline().strip()) for _ in range(N)]
list_visit = [[0]*M for _ in range(N)]
list_visit[0][0] = 1
list_queue = deque()
list_queue.append([0,0,0,1])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
end = 0
while list_queue:
    print('========================')
    [print(a) for a in list_visit]
    print(list_queue)
    now_x, now_y, check_turn, turn, result = list_queue.popleft()
    
    if now_x == M-1 and now_y == N-1:
        end = result
        break

    for i in dict_door[list_map[now_y][now_x]]:
        nx = now_x + dx[i]
        ny = now_y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if not list_visit[ny][nx] and 
    """
            if (check_turn and (list_map[now_y][now_x] == list_map[ny][nx] or list_map[ny][nx] == 'A') and not list_visit[ny][nx]) or (check_turn == 0 and ((list_map[ny][nx] == 'C' and i<=1) or (list_map[ny][nx] == 'D' and i>1) or list_map[ny][nx] == 'A') and not list_visit[ny][nx]):
                new_turn = check_turn
                list_queue.append([nx,ny,new_turn,result+1])
                list_visit[ny][nx] = result
    """
    """
    for i in list_door[check_turn-1][list_map[now_y][now_x]]:
        nx = now_x + dx[i]
        ny = now_y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if (check_turn and ((list_map[ny][nx] == 'C' and i<=1) or (list_map[ny][nx] == 'D' and i>1) or list_map[ny][nx] == 'A') and not list_visit[ny][nx]) or (check_turn == 0 and (list_map[now_y][now_x] == list_map[ny][nx] or list_map[ny][nx] == 'A') and not list_visit[ny][nx]):
                new_turn = (check_turn + 1)%2
                list_queue.append([nx,ny,new_turn,result+2])
                list_visit[ny][nx] = result
    """
if end:
    print(end)
else:
    print(-1)

            
            
"""
        if i <= 3:
            if (list_map[now_y][now_x] == 'A') or (list_map[now_y][now_x] == 'C' and i>=2) or (list_map[now_y][now_x] == 'D' and i<2):
                nx = now_x + dx[i]
                ny = now_y + dy[i]
                if 0 <= nx < M and 0 <= ny < N:
                    if list_map[ny][nx] == 'A' or (list_map[ny][nx] == 'C' and i>=2) or (list_map[ny][nx] == 'D' and i<2):
                        if not list_visit[ny][nx]:
                            22
        else:
            pass
"""
