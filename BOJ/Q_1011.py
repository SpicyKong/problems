# https://www.acmicpc.net/problem/1011 문제 제목 : Fly me to the Alpha Centauri , 언어 : Python, 날짜 : 2020-01-05, 결과 : 성공
# 겁나 삽질했다.. 어렵다

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    distance = y - x
    before_distance = 0
    n = 1
    while True:
        if not n % 2 == 0:
            if before_distance < distance <= (n//2)*(n//2+1) + n//2 + 1 :
                break
            else:
                before_distance = (n//2)*(n//2+1) + n//2 + 1
        else:
            if before_distance < distance  <= n//2 * (n//2 + 1):
                break
            else:
                before_distance = n//2 * (n//2 + 1)
        n+=1
    print(n)
