# https://www.acmicpc.net/problem/3101 문제 제목 : 토끼의 이동 , 언어 : Python, 날짜 : 2019-11-25, 결과 : 실패
# 메모리 초과 > 식세워서 풀어보기

import sys

N, K = map(int, sys.stdin.readline().split())
list_jump = list(sys.stdin.readline())

list_a = [[0]*N for _ in range(N)]
x, y = 0, 0
mode = 0 # 0=아래로 1=위로
for i in range(1, N**2+1):
    list_a[y][x] = i
    if not mode:
        if y == 0:
            x+=1
            mode = 1
        elif x == N-1:
            y+=1
            mode = 1
        else:
            y-=1
            x+=1
    else:
        if y == N-1:
            x+=1
            mode = 0
        elif x == 0:
            y+=1
            mode = 0
        else:
            x-=1
            y+=1
now_x, now_y = 0,0
result = 0
for direction in list_jump:
    result += list_a[now_y][now_x]
    if direction == 'D':
        now_y += 1
    elif direction == 'U':
        now_y -= 1
    elif direction == 'R':
        now_x += 1
    elif direction == 'L':
        now_x -= 1
print(result)
