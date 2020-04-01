# https://www.acmicpc.net/problem/1916 문제 제목 : 최소비용 구하기 , 언어 : Python, 날짜 : 2020-04-01, 결과 : 성공
"""
    회고:
    다익스트라 문제이다. 다익스트라 문제를 안풀어본건 오랜만에 풀어보니 다음 노드 선정을 어떻게 해야할지 감이 안잡혔다.
    결국 정석은 아니지만 그냥 인덱스 순서대로 방문가능 한 정점에 방문을 했다.

    이 문제를 풀면서 가장 막혔던 부분은 아직도 이유는 모르겠는데 list_cost라는 리스트에서 값을 -1로 초기화 해주고 처리하면 계속 틀렸다.
    그래서 V*E + 1값으로 초기화를 해보고 제출했더니 정답이였다. 이유는 모르겠다..
    아 그리고 이번에는 그냥 구현되어있는 운선순위큐를 사용했다.
"""

import sys
import heapq

def go(now_node, next_node):
    global list_map

def push(node, now_cost):
    global list_map, list_heap
    for cost,next_node in list_map[node]:
        heapq.heappush(list_heap, [cost+now_cost, next_node])

def next():
    global list_visit
    for i, visit in enumerate(list_visit):
        if not visit and list_map[i]:
            return i
    return 0

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
list_map = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int, sys.stdin.readline().split())
    list_map[a].append([c,b])
now_node, last_node = map(int, sys.stdin.readline().split())

list_visit = [0]*(N+1)
list_visit[0] = 1
list_visit[now_node] = 1

list_heap = []

list_cost = [100000000+1]*(N+1)
list_cost[now_node] = 0
push(now_node,list_cost[now_node])
while list_heap:
    cost, node2 = heapq.heappop(list_heap)

    if list_cost[node2] > cost:
        list_cost[node2] = cost
        list_visit[node2] = 0
    #else:

    
    if not list_heap:
        now_node = next()
        if now_node:
            push(now_node, list_cost[now_node])
            list_visit[now_node] = 1

print(list_cost)
"""
7
11
1 2 47
1 3 69
2 4 57
2 5 124
3 4 37
3 5 59
3 6 86
4 6 27
4 7 94
5 7 21
6 7 40
1 7

5
2
3 5 3
3 5 0
3 5

4
5
1 2 3
1 3 3
1 4 1
4 2 1
4 3 1
1 4

4
4
1 2 0
1 3 0
1 4 3
3 4 0
1 4
"""
