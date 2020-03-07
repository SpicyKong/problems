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
###############################################################################################################
# https://www.acmicpc.net/problem/1753 문제 제목 : 최단경로 , 언어 : Python, 날짜 : 2020-03-07, 결과 : 성공
"""
    회고:
    달라진 점이 3가지가 있다. heapq모듈을 사용함, INF를 스트링이아닌 정수로 선언해둠, 마지막으로 이유는 모르겠지만
    갱신할때 비교하는 조건문에서 list_result에 기록되어있는 값을 사용했는데 이번에는 그냥 큐에 넘겨주는 값을 바로사용했다.
    사실 이건 정답코드를 찾아보며 고친것이긴 한데 시간차이가 많이난다. 이유는 생각해봐야 알것 같다.
    + 오늘 여러문제 풀고 한번에 올려야지 하고 깜빡했다.. 아마도 로컬환경에 깃을 설치안해서 더욱 번거로운것 같다. 한번 환경을 구성해봐야 할것 같다.
    오늘은 프로그래머스에서 문제를 4개 더 풀었다.
"""

import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
INF = 10*(V - 1) + 1
start = int(sys.stdin.readline())
list_graph = [[] for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    list_graph[u-1].append([w,v-1])
list_result = [INF]*V
list_result[start-1] = 0

list_queue = []
heapq.heappush(list_queue, [0,start-1])
while list_queue:
    now_node = heapq.heappop(list_queue)
    for next_node in list_graph[now_node[1]]:
        if list_result[next_node[1]] > now_node[0] + next_node[0]:
            list_result[next_node[1]] = now_node[0] + next_node[0]
            heapq.heappush(list_queue, [list_result[next_node[1]], next_node[1]])
[print('INF') if result == INF else print(result) for result in list_result]
