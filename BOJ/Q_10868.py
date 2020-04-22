# https://www.acmicpc.net/problem/10868 문제 제목 : 최솟값 , 언어 : Python, 날짜 : 2020-04-22, 결과 : 성공
"""
    회고:
    세그먼트 트리를 복기하며 한번 다시 풀어 보았다. 세그먼트 트리를 알고 있다면 간단하다.
    하지만 체감상 오랜만에 다시 풀어봐서 그런지 약간 버벅이긴 했다..
"""

import sys
def init(start, end, node):
    global N
    if start >= N:
        return list_graph[node]
    if start == end:
        list_graph[node] = list_num[start]
        return list_graph[node]
    mid = (start + end)//2
    list_graph[node] = min(init(start, mid, node*2), init(mid+1, end, node*2+1))
    return list_graph[node]

def get_min(start, end, left, right, node):
    if start > right or end < left:
        return 1000000000
    if left <= start and end <= right:
        return list_graph[node]
    mid = (start + end)//2
    return min(get_min(start, mid, left, right, node*2), get_min(mid+1, end, left, right, node*2+1))

N, M = map(int, sys.stdin.readline().split())
list_num = [int(sys.stdin.readline()) for _ in range(N)]
list_graph = [1000000000]*(N*4+1)
init(0, N-1, 1)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(get_min(0, N-1, a-1, b-1, 1))
