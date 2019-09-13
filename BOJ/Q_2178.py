# https://www.acmicpc.net/problem/2178 문제 제목 : 미로 탐색 , 언어 : Python, 날짜 : 2019-09-13, 결과 : 성공

import sys
N, M = map(int, sys.stdin.readline().split())
listMap = [list(sys.stdin.readline()) for _ in range(N)]
listCheck = [[0]*M for _ in range(N)]
end = False
x, y = 0, 0
discoverd = []
listCheck[y][x] = 1
discoverd.append([0,0])
while discoverd:
    x, y = discoverd.pop(0)
    if x < M-1 and listMap[y][x+1] == '1':
        if not listCheck[y][x+1]:
            listCheck[y][x+1] = listCheck[y][x] +1
            discoverd.append([x+1, y])
    if x > 0 and listMap[y][x-1] == '1':
        if not listCheck[y][x-1]:
            listCheck[y][x-1] = listCheck[y][x] +1
            discoverd.append([x-1, y])
    if y < N-1 and listMap[y+1][x] == '1':
        if not listCheck[y+1][x]:
            listCheck[y+1][x] = listCheck[y][x] +1
            discoverd.append([x, y+1])
    if y > 0 and listMap[y-1][x] == '1':
        if not listCheck[y-1][x]:
            listCheck[y-1][x] = listCheck[y][x] +1
            discoverd.append([x, y-1])
print(listCheck[N-1][M-1])
