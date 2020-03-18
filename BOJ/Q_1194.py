# https://www.acmicpc.net/problem/1194 문제 제목 : 달이 차오른다, 가자. , 언어 : Python, 날짜 : 2020-03-18, 결과 : 실패

import sys
from collections import deque
"""
    회고:
    새로운 키를 발견하면 그위치부터 다시 BFS를 해나가주면 될거라고 생각했다.
    하지만 청므에는 무언가 잘못된건지 내가 생각한 대로 동작하지 않았다. 
    알고보니 key를 큐에 저장하는 과정에서 모든 큐가 이어져있는(?) 상태가 되었다.
    그래서 다른쪽에서 새로운 키를 찾으면 전혀 상관없는 경로에서도 키를 찾은상태가 되는거다.
    하지만 이 부분을 고쳤음에도 계속 틀린다. 한번 다시 풀어봐야겠다.
"""



N, M = map(int, sys.stdin.readline().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
list_map = [list(sys.stdin.readline().strip()) for _ in range(N)]
list_visit = [[-1]*M for _ in range(N)]
dict_key = {chr(65+i):i for i in range(6)}
list_queue = deque()
break_token = 0
depth = 1
for y in range(N):
    for x in range(M):
        if list_map[y][x] == '0':
            list_queue.append([x,y,[0,0,0,0,0,0],0,0])
            list_visit[y][x] = 0
            break_token = 1
            break
    if break_token:
        break
end = 0
while list_queue:
    now_x, now_y, key, count_key,result = list_queue.popleft()
    if list_map[now_y][now_x] == '1':
        end = result
        break
    for i in range(4):
        nx = now_x + dx[i]
        ny = now_y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if (list_map[ny][nx] == '.' or list_map[ny][nx] == '0' or list_map[ny][nx] == '1') and list_visit[ny][nx] < count_key:
                list_queue.append([nx, ny, key[:],count_key,result+1])
                list_visit[ny][nx] = count_key
            elif 'A' <= list_map[ny][nx] <= 'F' and list_visit[ny][nx] < count_key:
                if key[dict_key[list_map[ny][nx]]]:
                    list_queue.append([nx, ny, key[:],count_key,result+1])
                    list_visit[ny][nx] = count_key
                    #print(key, count_key)
            elif 'a' <= list_map[ny][nx] <= 'f' and list_visit[ny][nx] < count_key:
                if key[dict_key[list_map[ny][nx].upper()]]:
                    list_queue.append([nx, ny, key[:],count_key,result+1])
                    list_visit[ny][nx] = count_key
                else:
                    new_key = key[:]
                    new_key[dict_key[list_map[ny][nx].upper()]] = 1
                    list_queue.append([nx, ny, new_key,count_key+1,result+1])
                    list_visit[ny][nx] = count_key+1

if not end:
    print(-1)
else:
    print(end)
