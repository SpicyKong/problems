# https://www.acmicpc.net/problem/1002 문제 제목 : 터렛 , 언어 : Python, 날짜 : 2019-11-06, 결과 : 성공

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    a,b,c = 0,0,0
    if r2 > r1:
        a,b,c = x1, y1, r1
        x1, y1, r1 = x2, y2, r2
        x2, y2, r2 = a, b, c
    d = ((x1-x2)**2 + (y1-y2)**2)
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif r1**2 >= d: # 내부
        if d < (r1-r2)**2:
            print(0)
        elif d == (r1-r2)**2:
            print(1)
        else:
            print(2)
    elif r1**2 < d: # 외부
        if d > (r1 +r2)**2:
            print(0)
        elif d == (r1 +r2)**2:
            print(1)
        else:
            print(2)
