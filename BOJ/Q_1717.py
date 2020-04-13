# https://www.acmicpc.net/problem/1717 문제 제목 : 집합의 표현 , 언어 : Python, 날짜 : 2020-04-13, 결과 : 성공
"""
    회고:
    분명 유니온 파인드를 들어도 보고 자료도 찾아보고 했던 기억은 있는데 정작 유니온 파인드에 대해서는 기억이 잘 안났다..
    오늘부터 진짜로 알고리즘을 공부하려고 기계적으로 문제만 풀어보는것이 아니라 알고있는/ 알아가는/ 알고싶은 알고리즘들에
    대해 찾아보고 정리하기로 했다. 오늘 안으로 크루스칼 알고리즘과 프림 알고리즘을 추가하고 관련 문제들을 풀어보아야겠다.
    뭔가 자꾸 BOJ에서 배움이 없이(?)문제만 풀고나니 공부법을 이리저리 바꿔보기로 했고 이 방법이 첫번째로 바뀌는 공부법이다.
    그리고 최근 코포 3개의 콘테스트에 참가해보았는데 자꾸만 1솔을 하게되어서 1차적으로 3솔을 안정적으로 할때까지만이라도 열심히 하기로 했다.
    이야기가 다른곳으로 샜는데 유니온 파인드의 파인드 부분에서 list_parent[node] = find(list_parent[node]) 이 부분은 굉장히 중요하다고 한다.
    왜냐하면 이 부분이 있어야 시간복잡도를 줄일수있다. (재귀로 구현되니 저 부분이 없으면 다음번에 탐색할때도 루트노드까지 왔다갔다 해야함.)
"""

import sys


def find(node):
    if list_parent[node] == node:
        return node
    list_parent[node] = find(list_parent[node])
    return list_parent[node]

def merge(a, b):
    a = find(a)
    b = find(b)
    
    if a == b:
        return
    
    list_parent[b] = a
    

n, m = map(int, sys.stdin.readline().split())
list_parent = [i for i in range(n+1)]

for _ in range(m):
    action, a, b = map(int, sys.stdin.readline().split())

    if action:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
    else:
        merge(a,b)
