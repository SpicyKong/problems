# https://www.acmicpc.net/problem/10423 문제 제목 : 전기가 부족해 , 언어 : Python, 날짜 : 2020-04-16, 결과 : 성공
"""
    회고:
    이 문제를 이해하기로는 발전소를 최상위 부모노드로 갖는다면 몇개의 MST가 만들어져도 상관없고 그저 비용에 상관쓰면 된다고 이해했는데
    다른 
    
    이 문제를 틀렸었는데 회고를 저기까지 작성하다가 내가 무엇을 해야하는지 깨달았다. 틀린 원인은 다른 MST에 추가되어 있는 노드를 따로 처리해주지 않았기 때문이다.
    이 문제는 몇개의 MST든 상관없으니 발전소를 최상위 부모노드로 가지고 최소의 비용으로 모든 노드를 MST에 포함시키면 되는 문제다.
    그래서 내가 최근에 풀었던 친구 네트워크의 코드를 빌려 썼다. 추가된 부분은 발전소를 만났을때 처리해주는 방식만 생각해 주면 된다.

    오늘은 정말 피곤하다. 4시간 자고 아침부터 약 2~3시간동안 요리하고 집안일을 한뒤, 운동을 했다.
"""
import sys

def find(node):
    if node == list_parent[node][0]:
        return node
    list_parent[node][0] = find(list_parent[node][0])

    return list_parent[node][0]

def union(node1, node2, cost):
    global count, ans
    node1 = find(node1)
    node2 = find(node2)
    if node1 == node2 or (node1 in isConnected and node2 in isConnected):
        return
    ans += cost
    if node2 in isConnected:
        list_parent[node1][0] = list_parent[node2][0]
        if list_parent[node1][1]:
            list_parent[node2][1]+=list_parent[node1][1]
            count+=list_parent[node1][1]
            list_parent[node1][1] = 0

    elif node1 in isConnected:
        list_parent[node2][0] = list_parent[node1][0]
        if list_parent[node2][1]:
            list_parent[node1][1]+=list_parent[node2][1]
            count+=list_parent[node2][1]
            list_parent[node2][1] = 0

    if list_parent[node1][1] < list_parent[node2][1]:
        list_parent[node1][0] = list_parent[node2][0]
        
        if list_parent[node1][1]:
            list_parent[list_parent[node1][0]][1]+=list_parent[node1][1]
            list_parent[node1][1] = 0

    else:
        list_parent[node2][0] = list_parent[node1][0]
        if list_parent[node2][1]:
            list_parent[list_parent[node2][0]][1]+=list_parent[node2][1]
            list_parent[node2][1] = 0
    
    
N, M, K = map(int, sys.stdin.readline().split())
list_parent = [[i,1] for i in range(N)]
isConnected = set()
list_edge = []
count = K
ans = 0
for city in list(map(int, sys.stdin.readline().split())):
    isConnected.add(city-1)

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    list_edge.append([w, u-1, v-1])
list_edge.sort()
for edge in list_edge:
    union(edge[1], edge[2],edge[0])
    
    #print(list_parent)
    #print(count)
    if count >= N:
        break
print(ans)
"""
6 9 2
2 5
1 2 5
1 4 100
1 3 6
2 4 2
3 4 6
3 5 5
4 5 100
4 6 4
5 6 3
"""
