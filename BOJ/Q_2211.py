# https://www.acmicpc.net/problem/2211 문제 제목 : 네트워크 복구 , 언어 : Python, 날짜 : 2020-04-19, 결과 : 성공
"""
    회고:
    낚였다. 나는 분명 MST를 공부하려고 MST로 분류되어 있는 이 문제를 풀어보았던건데 풀고나니 계속 틀려서
    질문게시판을 보니 MST가 아니라 다익스트라 였다. 그래서 다시 읽어보니 정말 다익스트라다.. 이 문제에 있는 2번조건이
    이 문제를 다익스트라로 만든것이다. (1번은 그냥 스패닝트리를 만들라는 이야기다.) 그래서 슈퍼컴퓨터인 1번노드를 기준으로 다익스트라를 해주면 된다.
    오랜만에 다익스트라를 구현해보니 정말 프림알고리즘과 유사하다. 코드 3줄정도만 고치면 프림알고리즘이 다익스트라가 된다.
    
    아 그리고 오늘 스터디에 사용할 매크로를 만드느냐 셀레니움을 하루종일 붙들고 있었다. 그동안 bs4밖에 사용해본적이 없었는데
    확실히 셀레니움이 유명한 만큼 배울만한 재미가 있는것 같다.
"""

import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
list_map = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    list_map[a].append([c, b])
    list_map[b].append([c, a])
list_queue = [[0,1,1]]
list_visit = [1001]*(N+1)
list_result = []
while list_queue:
    cost, now_node, now_from = heapq.heappop(list_queue)
    if list_visit[now_node] <= cost:
        continue
    list_visit[now_node] = cost
    if cost:
        list_result.append([now_node, now_from])
    for next_node in list_map[now_node]:
        if list_visit[next_node[1]] > next_node[0]+cost:
            heapq.heappush(list_queue, [next_node[0]+cost, next_node[1], now_node])
print(len(list_result))
[print(*result) for result in list_result]
"""
4 5
1 2 1
1 3 2
1 4 3
2 3 1
3 4 1
"""
