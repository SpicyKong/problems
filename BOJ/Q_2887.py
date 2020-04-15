# https://www.acmicpc.net/problem/2887 문제 제목 : 행성 터널 , 언어 : Python, 날짜 : 2020-04-14, 결과 : 성공

import sys

def find(node):
    if node == list_parent[node]:
        return node
    list_parent[node] = find(list_parent[node])
    return list_parent[node]

def union(node1, node2):
    node1 = find(node1)
    node2 = find(node2)
    if node1 == node2:
        return
    list_parent[node2] = node1

N = int(sys.stdin.readline())
list_map = [list(map(int, sys.stdin.readline().split()))+[i] for i in range(N)]
list_all = []
list_parent = [i for i in range(N)]

for i in range(3):
    list_map.sort(key = lambda x: x[i])
    for j in range(N-1):
        list_all.append([abs(list_map[j][i] - list_map[j+1][i]), list_map[j+1][3], list_map[j][3]])
list_all.sort()

result = 0
count = 0

for edge in list_all:
    if not find(edge[1]) == find(edge[2]):
        union(edge[1], edge[2])
        result += edge[0]
        count+=1
    if count >= N -1:
        break
print(result)
