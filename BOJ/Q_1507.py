# https://www.acmicpc.net/problem/1507 문제 제목 : 궁금한 민호 , 언어 : Python, 날짜 : 2020-05-01, 결과 : 성공   
"""
    회고:
    아 문제에서 -1을 출력하라는 조건을 제대로 이해하지 못해서 계속 삽질을 하다가 게시판을 보고 나서야 삽질을 멈췄다.
    플로이드는 중간점을 거치더라도 최소값이 되면 갱신을했다. 하지만 우리는 최소한의 도로만 사용해야하므로 돌아서 갈 수 있다면 돌아가야한다.
    그래서 플로이드를 이용해서 중간점을 거쳐가는 길이와 직접 연결된 길이가 같다면 직접 연결된 도로는 없애야 한다.
    이러다 보면 답이나온다. 
    그리고 -1을 출력하라는 말이 알고보니 문제에서 주어진 정보들이 각 노드간의 최소값으로 주어지지 않았을 경우를 찾아내라는 말이였다..
    이것도 모르고 계속 이상한 부분만 건드렸다..ㅠㅠ

    내일쯤이면 레몬과 라임묘목들이 도착할거같다. 집에서 레몬과 라임을 길러보고 싶어서 충동구매를 했지만 열심히 키워봐야 겠다.
"""

import sys
def solve():
    N = int(sys.stdin.readline())
    list_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    list_map1 = [[2000500]*N for _ in range(N)]
    list_check = [[2 if i == j else 0 for j in range(N)] for i in range(N)]
    set_path = set((i,j) for j in range(N) for i in range(N) if not i==j)

    for mid in range(N):
        for start in range(N):
            for end in range(N):
                if start == end or start == mid or mid == end:
                    continue
                if list_map[start][end] > list_map[start][mid] + list_map[mid][end]:
                    print(-1)
                    return
                if list_map[start][end] == list_map[start][mid] + list_map[mid][end] and not list_check[start][end]:
                    list_check[start][end] = 1
                    set_path.remove((start, end))

    result = 0
    while set_path:
        start, end = set_path.pop()
        set_path.remove((end, start))
        result += list_map[start][end]
        list_map1[start][end] = list_map[start][end]
        list_map1[end][start] = list_map[start][end]
    print(result)
    

solve()
