# https://www.acmicpc.net/problem/1414 문제 제목 : 불우이웃돕기 , 언어 : Python, 날짜 : 2020-05-06, 결과 : 성공
"""
    회고:
    문제를 보고 입력값을 이해하는데 한참 걸렸다.
    최소 스패닝 트리를 구성하고 구성하는데에 필요한 비용을 전체 간선들의 비용에서 빼주면 되는 문제였다.
    나는 프림알고리즘을 이용했다. 다만 한가지 실수 했던게 연결이 되지 않은 부분은 가중치를 10000000000로 두어서
    못가게 하려 했는데 실수로 전체 간선의 가중치 합에 저 값이 들어가 버려서 계속 틀렸었다..
    다행히 직접 케이스를 만들어보다가 발견하고 고쳤다. 오랜만에 프림알고리즘을 복습하게된 문제다.
"""

import sys
import heapq

def solve():
    dict_alpha = {chr(65+i):(i+1+26) for i in range(26)}
    for i in range(26):
        dict_alpha[chr(97+i)] = i+1
    dict_alpha['0'] = 10000000000
    N = int(sys.stdin.readline())
    list_visit = [0]*N
    count = N
    total = 0
    now_total = 0
    list_input = [list(sys.stdin.readline().strip()) for _ in range(N)]
    list_map = [[0]*N for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if not list_input[y][x] == '0':
                total += dict_alpha[list_input[y][x]]
            if y == x:
                continue
            list_map[y][x] = min(dict_alpha[list_input[y][x]], dict_alpha[list_input[x][y]])
    list_queue = [[0,0]]
    while list_queue:
        now_cost, now_node = heapq.heappop(list_queue)
        if list_visit[now_node]:
            continue
        now_total+=now_cost
        list_visit[now_node] = 1
        count-=1
        if not count:
            break
        for next_node in range(N): 
            if list_map[now_node][next_node] == 10000000000 or next_node == now_node:
                continue
            heapq.heappush(list_queue, [list_map[now_node][next_node], next_node])
    if count:
        print(-1)
    else:
        print(total-now_total)

solve()
"""
4
abcd
abcd
abcd
abcd
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4


"""
