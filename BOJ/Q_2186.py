# https://www.acmicpc.net/problem/2186 문제 제목 : 문자판 , 언어 : Python, 날짜 : 2020-06-28, 결과 : 성공

"""
    회고:
    쉬워보여서 건드렸는데 1차로는 문제를 잘못읽었고 2차로는 문제를 잘못이해했었다.
    그 다음 시도에서는 50% 부근에서 시간초과가 났었는데 왜그런지 고민하다 게시판을 참고해 답을 얻었다.
    문제는 메모이제이션이었다.
    내가 기존에 작성했던 코드에서는 메모이제이션 테이블의 초기값이 0이여서
    미방문된 곳도 0이고 다음 탐색시 길이 없는곳도 0이여서 탐색을 진행해야 하는지
    길이 없는건지 알 수 없어 다음 길이 없어도 탐색이 계속 진행되어 시간초과가 났던것이었다.
    그래서 초기값을 그냥 -1(탐색이 안된곳)로 설정하고 -1일때마다 dfs를 시켜주었더니 통과되었다.

    문제 태그는 bfs였는데 정작 dp+dfs로 푸는게 가장 이상적인 방법인것 같다.
"""

import sys
from collections import deque

def dfs(x, y, c):
    global list_map, list_memo
    if c == lenW-1:
        list_memo[y][x][c] = 1
        return
    list_memo[y][x][c] = 0
    for i in (0,1,2,3):
        for j in range(1,K+1):
            nx = x + dx[i]*j
            ny = y + dy[i]*j
            if 0<=nx<M and 0<=ny<N and list_map[ny][nx] == word[c+1]:
                if list_memo[ny][nx][c+1] == -1:
                    #list_memo[y][x][c] += list_memo[ny][nx][c+1]
                    #continue
                    dfs(nx, ny, c+1)
                list_memo[y][x][c] += list_memo[ny][nx][c+1]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
N, M, K = map(int, sys.stdin.readline().split())
list_map = [list(sys.stdin.readline().strip()) for _ in range(N)]
word = sys.stdin.readline().strip()
res = 0
lenW = len(word)
list_start = []
list_memo = [[[-1]*lenW for _ in range(M)] for _ in range(N)]

for y in range(N):
    for x in range(M):
        if word[0] == list_map[y][x]:
            list_start.append((x,y))
            list_memo[y][x][0] = 0

for sx, sy in list_start:
    dfs(sx, sy, 0)
    res+=list_memo[sy][sx][0]
print(res)
#[print(a) for a in list_memo]
