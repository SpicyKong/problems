# https://www.acmicpc.net/problem/4195 문제 제목 : 친구 네트워크 , 언어 : Python, 날짜 : 2020-04-14, 결과 : 성공
"""
    회고:
    어제 유니온 파인드를 공부해서 곧바로 크루스칼과 프림알고리즘을 공부하려했는데 코드포스가 또 있었다..
    이 문제는 파이썬을 사용하면 정말 간단한 문제인거 같다. dictionary자료형이 정말 편하다. 이 문제는 기존에 1, 2, .. ,N 이런식으로 노드의 이름을 가졌던 문제들과 달리
    그냥 해시테이블에 추가해주고 사용하면 된다. 그리고 한가지, 내가 이 문제를 풀기위해 했던 방법은 내가 속해있는 트리의 최상위 루트 노드에 노드 수를 계속 더해주었다.

    온라인 강의를 들을수 있는 유일한 시간인 새벽에 코드포스를 하니깐 이번주차 온라인 강의를 다 들을 수 있을지 조차 의문이 생겨서
    우선 그 주의 온라인 수업을 어느정도 끝내고 여유가 있을 경우에 코드포스를 참여해야겠다. 만약 이러지 못했다면 다음날 버츄얼을 돌려봐야겠다.
"""
import sys

def find(node):
    if node == dict_parent[node][0]:
        return node
    dict_parent[node][0] = find(dict_parent[node][0])

    return dict_parent[node][0]
def getNum(name):
    if name == dict_parent[name][0]:
        return dict_parent[name][1]

    return getNum(dict_parent[name][0])
def union(node1, node2):
    global ans
    node1 = find(node1)
    node2 = find(node2)
    if node1 == node2:
        return
    if dict_parent[node1][1] < dict_parent[node2][1]:
        dict_parent[node1][0] = dict_parent[node2][0]
        if dict_parent[node1][1]:
            dict_parent[dict_parent[node1][0]][1]+=dict_parent[node1][1]
            dict_parent[node1][1] = 0
    else:
        dict_parent[node2][0] = dict_parent[node1][0]
        if dict_parent[node2][1]:
            dict_parent[dict_parent[node2][0]][1]+=dict_parent[node2][1]
            dict_parent[node2][1] = 0
    
    
T = int(sys.stdin.readline())
for _ in range(T):
    F = int(sys.stdin.readline())
    ans = 0
    dict_parent = {}
    for _ in range(F):
        f1, f2 = sys.stdin.readline().split()
        if not f1 in dict_parent:
            dict_parent[f1] = [f1,1]
        if not f2 in dict_parent:
            dict_parent[f2] = [f2,1]
        union(f1, f2)
        print(getNum(f1))
