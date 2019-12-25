# https://www.acmicpc.net/problem/2169 문제 제목 : 로봇 조종하기 , 언어 : Python, 날짜 : 2019-12-25, 결과 : 실패

import sys
N, M = map(int, sys.stdin.readline().split())
list_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
list_memo = [[[0,0]]*M for _ in range(N)]

for y in range(N):
    list_memo_x = [0]*M
    for x in range(M):
        if y == 0 and x == 0:
            pass
        elif y == 0:
            list_map[y][x] += list_map[y][x-1]        
        else:
            if x == 0:
                first2last = list_map[y-1][x]
                if list_memo_x[x] < first2last:
                    list_memo_x[x] = first2last
                last2first = max(list_map[y][M-1 - (x+1)], list_map[y-1][M-1-x])
                if list_memo_x[M-x-1] < last2first:
                    list_memo_x[M-x-1] = last2first
            elif x == M-1:
                last2first = list_map[y-1][x]
                if list_memo_x[M-x-1] < last2first:
                    list_memo_x[M-x-1] = last2first
                first2last = max(list_map[y][x-1],list_map[y-1][x])
                if list_memo_x[x] < first2last:
                    list_memo_x[x] = first2last
            else:
                first2last = max(list_map[y][x-1], list_map[y][x+1], list_map[y-1][x])
                if list_memo_x[x] < first2last:
                    list_memo_x[x] = first2last
                last2first = max(list_map[y][M-1 - (x-1)], list_map[y][M-1 - (x+1)], list_map[y-1][M-1-x])
                if list_memo_x[M-x-1] < last2first:
                    list_memo_x[M-x-1] = last2first
    for x in range(M):
        list_map[y][x] += list_memo_x[x]

    



[print(a) for a in list_map]

"""

1 1 1 0
0 0 1 0
0 0 0 0
0 0 0 0

"""

"""
        elif x == 0:
            first2last = max(list_map[y][x+1], list_map[y-1][x])
            last2first = max(list_map[y][M-1 - (x-1)], list_map[y-1][M-1-x])
            if list_memo_x[x] < first2last:
                list_memo_x[x] = first2last
            if list_memo_x[M-x-1] < last2first:
                list_memo_x[M-x-1] = last2first
        elif x == M-1:
            first2last = max(list_map[y][x-1], list_map[y][x+1], list_map[y-1][x])
            last2first = max(list_map[y][M-1 - (x-1)], list_map[y][M-1 - (x+1)], list_map[y-1][M-1-x])
            if list_memo_x[x] < first2last:
                list_memo_x[x] = first2last
            if list_memo_x[M-x-1] < last2first:
                list_memo_x[M-x-1] = last2first
"""
