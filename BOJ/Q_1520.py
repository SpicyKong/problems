# https://www.acmicpc.net/problem/1520 문제 제목 : 내리막 길 , 언어 : Python, 날짜 : 2020-04-04, 결과 : 성공
"""
    회고:
    가장 막혔던 부분은 탑다운 방식의 생각을 코드로 구현해 내는 부분인것 같다.
    그래서 다른분들이 어떻게 구현했는지만 참고했다. (아무리 생각해도 탑다운방식이 익숙해 지지 않는다.ㅠㅠ)
    이 문제는 만약 기존에 방문한적이 있다면 그 사실을 이용하면 된다. 그냥 직접 모든 경로를 찾으려면 시간초과를 피하기 쉽지 않기때문에
    앞서 말한대로 기존의 방문 여부를 메모이제이션에 활용해주면 된다.

    오늘 2만원이라는 거금을 가지고 데스크 매트를 주문했다. 오늘은 토요일이니 다음주 안으로 오면 좋겠다.

"""

import sys
sys.setrecursionlimit(10000)
def dfs(x, y):
    global list_map, list_memo
    if list_memo[y][x] == -1:
        list_memo[y][x] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if list_map[y][x] > list_map[ny][nx]:
                    list_memo[y][x] += dfs(nx, ny)
    return list_memo[y][x]

N, M = map(int, sys.stdin.readline().split())
list_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
list_memo = [[-1]*M for _ in range(N)]
list_memo[N-1][M-1] = 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dfs(0,0)
print(list_memo[0][0])
#[print(a) for a in list_memo]
