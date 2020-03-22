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
##########################################################################################################
# https://www.acmicpc.net/problem/2169 문제 제목 : 로봇 조종하기 , 언어 : Python, 날짜 : 2020-03-23, 결과 : 성공
"""
    회고:
    맨 처음에 생각한 방법은 현재칸인 (x,y)로 올수있는 방법은 (x-1,y) (x,y-1) (x+1,y) 이렇게 총 3가지임을 생각하고 문제를 풀었다.
    하지만 간과 했던 부분이 단순히 저렇게만 생각하고 메모이제이션을 하니깐 문제점이 발생했다.
    문제점은 메모이제이션을 해주는 배열에서 내가 지나온길의 보상이 더해진값을 보상으로 얻을수있는점이였다.
    그래서 생각한 방법은 왼쪽에서 출발하는 보상과 오른쪽에서 출발하는 보상을 각각 따로 저장해주는것이다.
    
    하지만 모든걸 해결하고 정답인줄알고 제출했지만 60퍼센트 부근에서 틀렸다.
    그래서 질문게시판을 보니 내가 list_visit배열을 초기화해줄때 0으로 초기화를 했던것이였다.
    이 문제에서는 주어지는 값의 절대값이 100보다 작다했으니 음수끼리 합해지면 초기화를 해줄때에도
    좀 많이 작은 수로 초기화를 해줘야한다.
    이 문제는 아까문제에 비해 생각보다 빨리풀려서 기분이 좋다.
    
    지금 보니 작년 12월25일 이 문제를 시도했었다!
"""

import sys


N, M = map(int, sys.stdin.readline().split())
list_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
list_visit = [[[-2e9,-2e9] for _ in range(M)] for _ in range(N)]
#[print(a) for a in list_visit]
list_visit[0][0][0] = list_map[0][0]
for x in range(1,M):
    list_visit[0][x][0] = list_visit[0][x-1][0] + list_map[0][x]
for y in range(1,N):
    for x in range(M):
        if x:
            list_visit[y][x][0] = max(list_visit[y][x-1][0], max(list_visit[y-1][x])) + list_map[y][x]
        else:
            list_visit[y][x][0] = max(list_visit[y-1][x]) + list_map[y][x]
    for x in range(M-1, -1, -1):
        if x < M-1:
            list_visit[y][x][1] = max(list_visit[y][x+1][1], max(list_visit[y-1][x])) + list_map[y][x]
        else:
            list_visit[y][x][1] = max(list_visit[y-1][x]) + list_map[y][x]
print(max(list_visit[N-1][M-1]))
