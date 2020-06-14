# https://www.acmicpc.net/problem/3109 문제 제목 : 빵집 , 언어 : Python, 날짜 : 2020-06-14, 결과 : 실패
"""
    회고:
    이 문제를 어떻게 백트레킹으로 접근해야하는지 잘 모르겠다. 그냥 그리디하게 위쪽부터 탐색하면 답이 나올 줄 알았는데,
    그렇게 쉬운 문제는 아니었다. 어떻게 푸는건지 좀 더 고민하고 내일 다시 풀어봐야겠다.
"""

import sys

R, C = map(int, sys.stdin.readline().split())
list_map = [list(sys.stdin.readline().strip()) for _ in range(R)]
list_visit = [[-1]*C for _ in range(R)]
dict_check = {x:0 for x in range(R)}
dict_check[-1]=0
result = 0
list_stack = [(0,0,0)]

while list_stack:
    now_x, now_y, start = list_stack.pop()
    if now_x == C-1:
        result+=1
        dict_check[start] = 1
        if start+1<R:
            list_stack.append((0,start+1, start+1))
        continue
    token = 0
    for i in (-1, 0, +1):
        ny = now_y + i
        if 0<=ny<R and not dict_check[list_visit[ny][now_x+1]] and list_map[ny][now_x+1]=='.':
            list_visit[ny][now_x+1] = start
            list_stack.append((now_x+1, ny,start))
            token = 1
            break
    if not token and start+1<R:
        list_stack.append((0,start+1, start+1))
        dict_check[start] = 0

print(result)
#[print(a) for a in list_visit]
