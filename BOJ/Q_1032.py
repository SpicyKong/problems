# https://www.acmicpc.net/problem/1032 문제 제목 : 명령 프롬프트 , 언어 : Python, 날짜 : 2019-10-27, 결과 : 성공

import sys
N = int(sys.stdin.readline())
list_str = list(sys.stdin.readline()[:-1])
for _ in range(N-1):
    for n,str_b in enumerate(sys.stdin.readline()[:-1]):
        if not list_str[n] == str_b:
            list_str[n] = '?'
print(''.join(list_str))
