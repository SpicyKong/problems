# https://www.acmicpc.net/problem/1697 문제 제목 : 숨바꼭질 , 언어 : Python, 날짜 : 2019-09-21, 결과 : 성공
# 맨 처음 배열을 100001까지만 선언했다가 다른분들의 질문글을 보다가 깨달았다..
# 그 부분을 고치니 맞게 되었다.

import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
end = False
list_queue = deque()
list_map = [0 for _ in range(200001)]
if 0 <= N-1 < 200001 and not list_map[N-1] == 1:
    list_queue.append(N-1)
    list_map[N-1] = 1
if 0 <= N+1 < 200001 and not list_map[N+1] == 1:
    list_queue.append(N+1)
    list_map[N+1] = 1
if 0 <= N*2 < 200001 and not list_map[N*2] == 1:
    list_queue.append(N*2)
    list_map[N*2] = 1
if N==K:
    end = True
list_map[K] = 2
count_queue = len(list_queue)
count_save = 0
count_time = 0
while not end:
    count_inQueue = 0
    while True:
        N = list_queue.popleft()
        if N == K:
            end = True
            break
        if 0 <= N-1 < 200001 and not list_map[N-1] == 1:
            list_queue.append(N-1)
            list_map[N-1] = 1
            count_save += 1
        if 0 <= N+1 < 200001 and not list_map[N+1] == 1:
            list_queue.append(N+1)
            list_map[N+1] = 1
            count_save += 1
        if 0 <= N*2 < 200001 and not list_map[N*2] == 1:
            list_queue.append(N*2)
            list_map[N*2] = 1
            count_save += 1
        count_inQueue+=1
        if count_inQueue>=count_queue:
            break
    count_queue = count_save
    count_save = 0
    count_time +=1
print(count_time)
