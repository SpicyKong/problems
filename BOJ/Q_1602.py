# https://www.acmicpc.net/problem/1602 문제 제목 : 도망자 원숭이 , 언어 : Python, 날짜 : 2020-04-20, 결과 : 성공 
"""
    회고:
    플로이드 워셜은 처음 공부해보는데 대충 느낌을 알아가는것 같다. 근데 이 문제는 약간 함정이 숨어 있어서 삽질을 했다.
    이 문제의 가장 큰 함정은 멍멍이다. 멍멍이가 괴롭히는 시간을 잘 처리해 주지 않으면 나 처럼 틀린다. 왜냐하면 무조건 멍멍이가 괴롭히는시간과 이동시간을 합쳐서 최소가 되는것만 찾는다면
    다음번에 갑자기 멍멍이가 엄청 괴롭히면 내가 찾아낸 최단 경로가 무용지물이 될 수도 있기 때문이다. 나는 다른분의 질문을 보고 답을 알았는데
    그렇기 때문에 멍멍이가 조금만 괴롭히는 순서대로 탐색을 해 나가면 이 문제를 해결 할 수 있다. 참고로 이 문제의 질문 게시판에 나온 질문의 대부분이 이 이야기였다.
    
    플로이드 워셜 알고리즘: 모든 정점간의 최단경로를 구할때 사용함. O(N^3)
"""
import sys
N, M, Q = map(int, sys.stdin.readline().split())
list_stress = list(map(int, sys.stdin.readline().split()))
list_stress1 = [[list_stress[i], i] for i in range(N)]
list_stress1.sort()
INF = 10000600000
list_cost = [[[INF,max(list_stress[i], list_stress[j])] for j in range(N)] for i in range(N)]

for _ in range(M):
    a, b, d = map(int, sys.stdin.readline().split())
    if list_cost[a-1][b-1][0] > d:
        list_cost[a-1][b-1][0] = d
        list_cost[b-1][a-1][0] = d

for i in range(N):
    list_cost[i][i][0] = 0


for through in range(N):
    through = list_stress1[through][1]
    for start in range(N):
        for end in range(N):
            if list_cost[start][end][0] + list_cost[start][end][1] > list_cost[start][through][0] + list_cost[through][end][0] + max(list_cost[start][through][1], list_cost[through][end][1]):
                list_cost[start][end][0] = list_cost[start][through][0] + list_cost[through][end][0]
                list_cost[start][end][1] = max(list_cost[start][through][1], list_cost[through][end][1])

for _ in range(Q):
    a, b = map(int, sys.stdin.readline().split())
    a-=1
    b-=1
    if INF <= sum(list_cost[a][b]):
        print(-1)
    else:
        print(sum(list_cost[a][b]))
"""
7 8 5
2 3 5 15 4 4 6
1 2 20
1 4 80
1 5 50
2 3 10
3 5 10
3 5 10
4 5 15
6 7 10
1 5
1 6
5 1
3 1
6 7

"""
