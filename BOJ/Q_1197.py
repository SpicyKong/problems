# https://www.acmicpc.net/problem/1197 문제 제목 : 최소 스패닝 트리 , 언어 : Python, 날짜 : 2020-04-12, 결과 : 성공
"""
    회고:
    프림 알고리즘을 배워보았다. 프림 알고리즘은 우선순위큐를 이용하여 현재 방문할수있는 정점중 가장 최소비용순서대로 방문하는 알고리즘이다.
    예전에 크루스칼 알고리즘을 배워본적이 있었는데 한번 이 문제를 크루스칼 알고리즘으로도 풀어보고 정리해야겠다.
"""

import sys
import heapq
V, E = map(int, sys.stdin.readline().split())
list_vertex = [[] for _ in range(V)]
for _ in range(E):
    a,b, cost = map(int, sys.stdin.readline().split())
    list_vertex[a-1].append([cost, b-1])
    list_vertex[b-1].append([cost, a-1])

list_visit = [0]*V

list_queue = [[0,0]]
result = 0
while list_queue:
    cost, now_node = heapq.heappop(list_queue)
    if list_visit[now_node]:
        continue
    list_visit[now_node] = 1
    result+=cost
    for node in list_vertex[now_node]:
        heapq.heappush(list_queue, node)
print(result)
