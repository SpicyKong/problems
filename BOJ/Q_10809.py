# https://www.acmicpc.net/problem/10809 문제 제목 : 알파벳 찾기 , 언어 : Python, 날짜 : 2019-11-12, 결과 : 성공

import sys

s = list(sys.stdin.readline()[:-1])
len_a = len(s)
#print(ord('a'), ord('z'))
list_a = [0]*(26)
for n in range(26):
    w = chr(97+n)
    for i, c in enumerate(s):
        if c == w:
            list_a[n] = i
            break
        elif i == len_a-1:
            list_a[n] = -1
print(*list_a)
# 97 122
