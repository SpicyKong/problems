# https://www.acmicpc.net/problem/10250 문제 제목 : ACM 호텔 , 언어 : Python, 날짜 : 2019-12-18, 결과 : 성공

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    floor = str(N%H)
    num = str((N-1)//H+1)
    if floor == '0':
        floor = str(H)
    if len(num) == 1:
        num = '0' + num
    print(floor + num)
