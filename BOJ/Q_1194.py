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
#####################################################################################
# https://www.acmicpc.net/problem/1194 문제 제목 : 달이 차오른다, 가자. , 언어 : Python, 날짜 : 2020-03-19, 결과 : 실패
"""
    회고:
    비트마스크를 적용해서 풀어보는데 기본테케도 틀린다..ㅠㅠ 지금 부터 맞힐때까지 시도해야겠다.
    오늘은 과제하고 강의도 들었지만 생각보다 빨리 끝나서 여유를 부렸는데 생각보다 PS하는 시간이 늦어졌다. 내일부턴 오전중에 PS를 시작해봐야겠다.
    아그리고 낮만 되면 강의서버가 터져서 오늘은 5시에 알람을 맞추고 6시에 일어났다. 강의를 듣기전 실시간 검색어를 봤는데 좋은 이야기가 하나도 없다.
    이놈의 코로나..
아래는 그때 실시간 검색어다.
1 배우 문지윤                     태풍급 강풍 
2 바흐 IOC 위원장                 이탈리아 하루 만에 475명 사망 
3 급성 패혈증으로 사망             중국 바이러스 
4 IOC 무책임하다                   누적 사망자 2천978명 
5 한국이 더 안전                   뉴욕 증시 폭락 
6 라디오스타 김민아                코로나19 사태 
7 펜싱 국가대표                    코로나19 여파 
8 PGA 챔피언십도 연기              오늘의 날씨 
9 티켓 환불 불가                   미국 코로나19 환자 7천명 넘어 
10 나는 트로트 가수다 설하윤        WTI 24% 대폭락
"""

import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]
N, M = map(int, sys.stdin.readline().split())
list_map = [list(sys.stdin.readline().strip()) for _ in range(N)]
list_visit = [[[0,0] for _ in range(M)] for _ in range(N)]
list_queue = deque()
dict_key = {chr(65+i):i for i in range(6)}
break_token = 0
for y in range(N):
    for x in range(M):
        if list_map[y][x] == '0':
            list_visit[y][x] = [1, 0]
            list_queue.append([x,y,0,0])
            break_token = 1
            break
    if break_token:
        break
end = 222222222222222222
while list_queue:
    now_x, now_y, key, result = list_queue.popleft()
    #print('============')
    #[print(a) for a in list_visit]
    #print(now_x, now_y)
    if list_map[now_y][now_x] == '1':
        if result < end:
            end = result
    for i in range(4):
        nx = now_x + dx[i]
        ny = now_y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            #print('key', key | list_visit[ny][nx][1], key, list_visit[ny][nx][1])
            # not key == list_visit[ny][nx][1]
            if (list_map[ny][nx] == '0' or list_map[ny][nx] == '1' or list_map[ny][nx] == '.') and (not list_visit[ny][nx][0] or not key == list_visit[ny][nx][1]) :
                list_queue.append([nx,ny,key,result+1])
                list_visit[ny][nx] = [1, key]
            elif 'a' <= list_map[ny][nx] <= 'f' and (not list_visit[ny][nx][0] or not key == list_visit[ny][nx][1]):
                key |= 1 << dict_key[list_map[ny][nx].upper()]
                list_queue.append([nx,ny,key,result+1])
                list_visit[ny][nx] = [1, key]
            elif 'A' <= list_map[ny][nx] <= 'F' and (not list_visit[ny][nx][0] or not key == list_visit[ny][nx][1]):
                i = dict_key[list_map[ny][nx]]
                check = 1 << i
                check = check & key
                check >> i
                if check:
                    list_queue.append([nx, ny, key, result+1])
                    list_visit[ny][nx] = [1, key]
            
if end == 222222222222222222:
    print(-1)
else:
    print(end)
#####################################################################################
# https://www.acmicpc.net/problem/1194 문제 제목 : 달이 차오른다, 가자. , 언어 : Python, 날짜 : 2020-03-20, 결과 : 성공
"""
    회고:
    아무리 생각해도 내가 전에 작성했던 코드의 논리의 흐름은 틀린게 없는것 같았다.
    그래서 생각해보니 두가지 문제점이 있었다.
    첫번째 문제점은 key값을 업데이트할때 얕은복사가 이루어져 전혀 상관없는 장소에서도 업데이트가 되었다.
    두번째 문제점은 새로운 키를 발견해 왔던길을 되돌아갈수 있도록 처리해주는 과정에서 조건을 현재 key와 visit에 저장된 키값이 다르면 갈수있도록 해준점이다.
    이 과정의 문제점은 만약 더 적은 키를 가지고 있음에도 계속 탐색을 진행하면서 무한루프에 빠지게 된다.
    그래서 다시 원래 생각했던 or연산을 통해 값이 커지는 경우에만 이동을 시키게 만들었다.

"""
import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]
N, M = map(int, sys.stdin.readline().split())
list_map = [list(sys.stdin.readline().strip()) for _ in range(N)]
list_visit = [[[0,0] for _ in range(M)] for _ in range(N)]
list_queue = deque()
dict_key = {chr(65+i):i for i in range(6)}
break_token = 0
for y in range(N):
    for x in range(M):
        if list_map[y][x] == '0':
            list_visit[y][x] = [1, 0]
            list_queue.append([x,y,0,0])
            break_token = 1
            break
    if break_token:
        break
end = 222222222222222222
while list_queue:
    now_x, now_y, key, result = list_queue.popleft()
    if list_map[now_y][now_x] == '1':
        if result < end:
            end = result
    for i in range(4):
        nx = now_x + dx[i]
        ny = now_y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if (list_map[ny][nx] == '0' or list_map[ny][nx] == '1' or list_map[ny][nx] == '.') and (not list_visit[ny][nx][0] or key | list_visit[ny][nx][1] > list_visit[ny][nx][1]):
                list_queue.append([nx,ny,key,result+1])
                list_visit[ny][nx] = [1, key]
            elif 'a' <= list_map[ny][nx] <= 'f' and (not list_visit[ny][nx][0] or key | list_visit[ny][nx][1] > list_visit[ny][nx][1]):
                new_key = key | 1 << dict_key[list_map[ny][nx].upper()]
                list_queue.append([nx,ny,new_key,result+1])
                list_visit[ny][nx] = [1, new_key]
            elif 'A' <= list_map[ny][nx] <= 'F' and (not list_visit[ny][nx][0] or key | list_visit[ny][nx][1] > list_visit[ny][nx][1]):
                i = dict_key[list_map[ny][nx]]
                check = 1 << i
                check = check & key
                check >> i
                if check:
                    list_queue.append([nx, ny, key, result+1])
                    list_visit[ny][nx] = [1, key]
            
if end == 222222222222222222:
    print(-1)
else:
    print(end)
