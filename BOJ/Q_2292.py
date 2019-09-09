# https://www.acmicpc.net/problem/2292 문제 제목 : 벌집 , 언어 : Python, 날짜 : 2019-09-09, 결과 : 성공

import sys

N = int(sys.stdin.readline())
if N==1:
    print(1)
else:
    a=1
    b=2
    c=0
    while True:
        c+=1
        if N-1 <= a*6:
            break
        a+=b
        b+=1
    print(c+1)
