# https://www.acmicpc.net/problem/11404 문제 제목 : 플로이드 , 언어 : Python, 날짜 : 2020-04-30, 결과 : 성공 
"""
    회고:
    플로이드 와샬을 까먹은거 같아 복습했다. 솔직히 알고리즘 이름만 듣고 알고리즘이 안떠오르고 그냥 희미하게
    반복문들이 떠올랐다. 그래서 결국 그냥 다시 찾아보고 공부했다. 내 기억력은 남들보다 더욱 안좋은것 같다. 메모나 필기하는 습관을
    들여야겠다.
"""

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
list_map = [[100000009]*n for _ in range(n)]

for _ in range(m):
    i, j, c = map(int, sys.stdin.readline().split())
    if c < list_map[i-1][j-1]:
        list_map[i-1][j-1] = c

for i in range(n):
    list_map[i][i] = 0
for mid in range(n):
    for start in range(n):
        for end in range(n):
            if list_map[start][end] > list_map[start][mid] + list_map[mid][end]:
                list_map[start][end] = list_map[start][mid] + list_map[mid][end]
for a in list_map:
    for cost in a:
        if cost >= 100000009:
            print(0, end=' ')
        else:
            print(cost, end=' ')
    print()
