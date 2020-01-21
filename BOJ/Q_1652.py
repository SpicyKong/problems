# https://www.acmicpc.net/problem/1652 문제 제목 : 누울 자리를 찾아라 , 언어 : Python, 날짜 : 2020-01-21, 결과 : 성공

import sys
N = int(sys.stdin.readline())
list_map = [list(sys.stdin.readline().strip()) for _ in range(N)]
count_now = 0
count_sero = 0
count_garo = 0
for y in range(N):
    for x in range(N):
        if list_map[y][x] == '.':
            count_now += 1
        if list_map[y][x] == 'X' or x == N-1:
            if count_now >= 2:
                count_garo += 1
            count_now = 0
    
for x in range(N):
    for y in range(N):
        if list_map[y][x] == '.':
            count_now += 1
        if list_map[y][x] == 'X' or y == N-1:
            if count_now >= 2:
                count_sero += 1
            count_now = 0
print(count_garo, count_sero)
