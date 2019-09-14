# https://www.acmicpc.net/problem/1012 문제 제목 : 유기농 배추 , 언어 : Python, 날짜 : 2019-08-25, 결과 : 실패
# https://www.acmicpc.net/problem/1012 문제 제목 : 유기농 배추 , 언어 : Python, 날짜 : 2019-09-14, 결과 : 성공
import sys

def contour():
    global x, y, list_field, list_visit
    queue_ismi = [[x, y]]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue_ismi:
        x, y = queue_ismi.pop(0)
        list_field[y][x] = 0
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0 <= ax < n and 0 <= ay < m:
                if list_field[ay][ax] and not list_visit[ay][ax]:
                    list_visit[ay][ax] = 1
                    queue_ismi.append([ax,ay])
t = int(sys.stdin.readline())
for _ in range(t):
    n, m, k = map(int, sys.stdin.readline()[:-1].split())
    list_field = [[0]*n for _ in range(m)]
    list_visit = [[0]*n for _ in range(m)]
    list_bechu = []
    for i in range(k):
        a, b = map(int, sys.stdin.readline().split())
        list_bechu.append([a, b])
        list_field[b][a] = 1
    count = 0
    for x,y in list_bechu:
        if list_field[y][x]==1:
            contour()
            count+=1
    print(count)
