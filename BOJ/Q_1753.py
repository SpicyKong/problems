# https://www.acmicpc.net/problem/1753 문제 제목 : 최단경로 , 언어 : Python, 날짜 : 2020-03-06, 결과 : 실패
"""
    회고:
    다익스트라 여러번 들어보기는 했지만 막상 짜보는건 처음이다. 단순히 BFS에서 큐에서 값을 뺄때만 주의해주면 될줄알았는데
    그런건 아닌가 보다. 더군다나 내가 사용했던 PriorityQueue를 이용해 우선순위큐를 구성하면
    값을 빼오는 메소드인 .get()을 쓸때 큐가 비어있으면 프로그램이 멈춰버린다.. 이유는 잘 모르겠지만..
    심지어 이 list_queue는 True와 False로 비교해도 둘중 아무것도 아니라고 한다. 그래서 while문 탈출도 못했다.
    큰일이다.
"""

import sys
from queue import PriorityQueue

V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
list_graph = [[] for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    list_graph[u-1].append([w,v-1])
list_result = ['INF']*V
list_result[start-1] = 0
list_queue = PriorityQueue()
list_queue.put((0,start-1))
count = 1

while count:
    now_w, now_node = list_queue.get()
    count -= 1
    for next_node in list_graph[now_node]:
        if list_result[next_node[1]] == 'INF' or list_result[next_node[1]] > list_result[now_node] + next_node[0]:
            list_result[next_node[1]] = list_result[now_node] + next_node[0]
            list_queue.put((next_node[0], next_node[1]))
            print((next_node[0], next_node[1]))
            count+=1
[print(result) for result in list_result]
