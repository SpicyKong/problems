# https://www.acmicpc.net/problem/9205 문제 제목 : 맥주 마시면서 걸어가기 , 언어 : Python, 날짜 : 2019-09-24, 결과 : 실패
# https://www.acmicpc.net/problem/9205 문제 제목 : 맥주 마시면서 걸어가기 , 언어 : Python, 날짜 : 2019-09-25, 결과 : 성공

import sys
from collections import deque
t = int(sys.stdin.readline())
state_store = []
state_fastiver = []
for _ in range(t):
    b_e = 0
    n = int(sys.stdin.readline())
    state_home = list(map(int, sys.stdin.readline().split()))
    state_store = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    state_fastiver = list(map(int, sys.stdin.readline().split()))
    if abs(state_home[0] - state_fastiver[0])+abs(state_home[1] - state_fastiver[1]) <= 1000:
        print("happy")
    else:
        list_queue = deque([i for i in range(n) if abs(state_home[0] - state_store[i][0])+abs(state_home[1] - state_store[i][1]) <= 1000])
        list_visit = [0 for _ in range(n)]
        while list_queue:
            x, y = state_store[list_queue.popleft()]
            if abs(x - state_fastiver[0])+abs(y - state_fastiver[1]) <= 1000:
                print('happy')
                b_e = 1
                break
            for i,j in enumerate(state_store):
                if abs(x - j[0])+abs(y - j[1]) <= 1000 and not list_visit[i]:
                    list_queue.append(i)
                    list_visit[i] = 1
        if b_e == 0:
            print('sad')
