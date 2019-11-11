# https://www.acmicpc.net/problem/8958 문제 제목 : OX퀴즈 , 언어 : Python, 날짜 : 2019-11-11, 결과 : 성공

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    count = 0
    result = 0
    list_a = list(sys.stdin.readline()[:-1])
    for c in list_a:
        if c == 'X':
            count = 0
        else:
            count+=1
            result += count
    print(result)
