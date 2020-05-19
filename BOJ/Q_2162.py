# https://www.acmicpc.net/problem/2162 문제 제목 : 선분 그룹 , 언어 : Python, 날짜 : 2020-05-19, 결과 : 성공
"""
    회고:
    맨 처음에 두 선분이 만난다는걸 어떻게 판단을 할까 하다가 ccw알고리즘을 이용하면 될거같았다.
    그래서 대충 생각을 해보다가 몇가지 반례에 대해서 도저히 풀이를 못하겠어서 인터넷에 검색을 해 보았다.
    그런데 ccw알고리즘을 사용하면 편하다는 글을 보았고, 그 글에서 나온 알고리즘을 이용했다.
    선분이 교차하는지 판정하는 함수를 만든 후 유니온 파인드를 이용해 선분의 그룹을 만들어 주었다.
    그런데 사실 내가 맨 처음 생각한 방법은 유니온을 해주며 노드의 개수가 가장 많은 그룹을 뽑아 주려 했는데, 계속 틀렸었다..
    그래서 혹시몰라 가장 마지막 for문에서 최대값을 구해 주었더니 맞았다. 이런 문제를 풀때 시간제한이 있었다면 절대 못풀거 같다..ㅠㅠ
"""

import sys
def ccw(a, b, c):
    return (b[0] - a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

def isCross(line1, line2):
    s1, s2 = line1
    s3, s4 = line2
    r1 = ccw(s1, s2, s3) * ccw(s1, s2, s4)
    r2 = ccw(s3, s4, s1) * ccw(s3, s4, s2)
    if (r1==0 and r2==0):
        if s1>s2:
            s1, s2 = s2, s1
        if s3>s4:
            s3, s4 = s4, s3
        return not (s2<s3 or s4<s1)
    return (r1 <=0 and r2<=0)

def find(node):
    if node == list_parent[node][0]:
        return node
    list_parent[node][0] = find(list_parent[node][0])
    return list_parent[node][0]

def union(node1, node2):
    node1 = find(node1)
    node2 = find(node2)
    if node1==node2:
        return
    if list_parent[node1][1] > list_parent[node2][1]:
        list_parent[list_parent[node1][0]][1] += list_parent[node2][1]
        list_parent[node2][1] = 0
        list_parent[node2][0] = list_parent[node1][0]
    else:
        list_parent[list_parent[node2][0]][1] += list_parent[node1][1]
        list_parent[node1][1] = 0
        list_parent[node1][0] = list_parent[node2][0]
    
N = int(sys.stdin.readline())
m = 0
list_parent = [[i, 1] for i in range(N)]
list_n=[0 for _ in range(N)]
list_line = []
for _ in range(N):
    x1, y1, x2, y2=map(int, sys.stdin.readline().split())
    list_line.append(((x1,y1),(x2, y2)))

for i in range(N-1):
    for j in range(i+1, N):
        if isCross(list_line[i], list_line[j]):
            union(i, j)
count = 0
#print(list_parent)
for i in range(N):
    i=find(i)
    if not list_n[i]:
        count+=1
    list_n[i]+=1
    m=max(m, list_n[i])
print(count)
print(m)
