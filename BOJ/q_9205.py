# https://www.acmicpc.net/problem/9205 문제 제목 : 맥주 마시면서 걸어가기 , 언어 : Python, 날짜 : 2019-09-24, 결과 : 실패

# 푸는중 입니다..
import sys
from collections import deque
t = int(sys.stdin.readline())
#state_home = []
state_store = []
state_fastiver = []
n = int(sys.stdin.readline())
for _ in range(t):
    state_home = list(map(int, sys.stdin.readline().split()))
    state_store = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    state_fastiver = list(map(int, sys.stdin.readline().split()))
    if abs(state_home[0] - state_fastiver[0])+abs(state_home[1] - state_fastiver[1]) <= 1000:
        print("happy")
    else:
        list_queue = deque()
        for i,j in enumerate(state_store):
            if abs(state_home[0] - j[0])+abs(state_home[1] - j[1]) <= 1000:
                list_queue.append(i)
                list_visit.append(1)
            else:
                list_visit.append(0)
        #list_queue = deque([i for i,j in enumerate(state_store) if abs(state_home[0] - j[0])+abs(state_home[1] - j[1]) <= 1000 ])
        #list_visit = 
        while list_queue:
            x, y = state_store[list_queue.popleft()]

