# https://www.acmicpc.net/problem/2357 문제 제목 : 최솟값과 최댓값 , 언어 : Python, 날짜 : 2020-04-18, 결과 : 성공
"""
    회고:
    어제 배웠던 세그먼트 트리를 복기해 가며 스스로 풀어 보았다. 이 문제는 노드마다 min, max값을 저장해두고 있으면 되는 문제다.
    만약 범위를 벗어나게 된다면 min값에 1000000000과 max값에 -1을 넣어서 벗어난 곳의 0,0
"""

import sys
def init(start, end, node):
    global N
    if start >= N:
        return [1000000000, -1]
    if start == end:
        list_graph[node] = [list_num[start], list_num[start]]
        return list_graph[node]
    mid = (start + end) // 2
    node_left = init(start, mid, node*2)
    node_right = init(mid+1, end, node*2+1)
    list_graph[node][0] = min(node_left[0], node_right[0])
    list_graph[node][1] = max(node_left[1], node_right[1])
    return list_graph[node]

def getmM(start, end, left, right, node):
    if start > right or end < left:
        return [1000000000, -1]
    if start >= left and right >= end:
        return list_graph[node]
    mid = (start + end)//2
    left_node = getmM(start, mid, left, right, node*2)
    right_node = getmM(mid+1, end, left, right, node*2+1)
    return [min(left_node[0], right_node[0]), max(left_node[1], right_node[1])]


N, M = map(int, sys.stdin.readline().split())
list_num = [int(sys.stdin.readline()) for _ in range(N)]
list_graph = [[0, 0] for _ in range(N*4+1)]
init(0, N-1, 1)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(*getmM(0, N-1, a-1, b-1, 1))
