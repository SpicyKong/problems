# https://www.acmicpc.net/problem/1922 문제 제목 : 네트워크 연결 , 언어 : Python, 날짜 : 2020-03-05, 결과 : 성공

import sys
"""
    회고:
    오늘부터 알고리즘을 공부하기로 했다. 오늘은 크루스칼 알고리즘을 공부했다.
    크루스칼 알고리즘은 최소비용으로 모든 노드를 연결하는 알고리즘이다. 그래서 항상 간선의 갯수는
    노드의 갯수 - 1 이라고 한다. 아, 그리고 크루스칼 알고리즘을 공부하기 전에 알아야 하는 개념이 하나 있다.
    바로 유니온 파인드이다. 두개의 노드가 서로 같은 그래프에 속하는지 판별하는 알고리즘(?)이다.

"""
def change_parent(p1, p2):
    global graph
    while graph[p2]:
        node = graph[p2].pop()
        graph[p1].append(node)
        list_check_cycle[node] = p1
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
list_info = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(M)], key = lambda a: a[2])
list_check_cycle = [i for i in range(N+1)]
graph = [[i] for i in range(N+1)]
result = 0
for info in list_info:
    if not list_check_cycle[info[0]] == list_check_cycle[info[1]]:
        min_value = list_check_cycle[info[0]]
        max_value = list_check_cycle[info[1]]
        if min_value > max_value:
            min_value = list_check_cycle[info[1]]
            max_value = list_check_cycle[info[0]]
        change_parent(min_value, max_value)
        result+=info[2]
print(result)
