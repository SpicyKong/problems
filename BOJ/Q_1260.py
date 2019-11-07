# https://www.acmicpc.net/problem/1260 문제 제목 : DFS와 BFS , 언어 : Python, 날짜 : 2019-11-07, 결과 : 실패

import sys
from collections import deque
sys.setrecursionlimit(10**6)


N, M, V = map(int, input().split())

list_graph = [set([]) for _ in range(N+1)] # 인접 리스트를 구현합니다.
for _ in range(M):
    i, j = map(int, input().split())
    list_graph[i].add(j)
    list_graph[j].add(i)


list_print_d = [V] # 탐색한 순서를 저장하는 리스트 입니다.
list_visit_d = [0]*(N+1) # 방문을 체크하는 리스트 입니다.
list_visit_d[V] = 1 # 시작지점은 방문체크 해 줍니다.
def dfs(root):
    global list_graph, list_print_d
    for num in list_graph[root]: # root에 연결되어 있는 노드를 차례대로 탐색합니다.
        if not list_visit_d[num]: # 만약에 탐색이 안된곳이면
            list_visit_d[num] = 1 # 방문처리를 해 주고
            list_print_d.append(num) # 탐색했던 순서를 저장하는 리스트에 추가해 줍니다.
            dfs(num) # 그리고 현재 노드에서 다시 dfs() 함수를 실행시킵니다.


list_print_b = [] # 탐색한 순서를 저장하는 리스트 입니다.
list_visit_b = [0]*(N+1) # 방문을 체크하는 리스트 입니다.
list_visit_b[V] = 1 # 시작지점은 방문체크 해 줍니다.
def bfs(root):
    global list_graph
    list_queue = deque([root]) # bfs는 큐를 이용해 구현했습니다.
    #list_queue.append(root)
    while list_queue:
        num = list_queue.popleft() # 큐에 있는 값을 pop해주고
        list_print_b.append(num) # 방문 순서를 기록하는 리스트에 추가합니다.
        for i in list_graph[num]: # 그리고 현재 노드에 연결된 노드들을 탐색합니다.
            if not list_visit_b[i]: # 만약 방문하지 않았다면
                list_visit_b[i] = 1 # 방문체크를 해주고
                list_queue.append(i) # 현재노드를 큐에 push해줍니다.

dfs(V)
bfs(V)
print(*list_print_d)
print(*list_print_b)

