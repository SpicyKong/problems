# https://www.acmicpc.net/problem/1105 문제 제목 : 팔 , 언어 : Python, 날짜 : 2019-11-27, 결과 : 성공

import sys
L, R = sys.stdin.readline().split()
result = 0
if not len(R) == len(L):
    pass
elif L == R:
    for i in range(len(R)):
        if R[i] == '8':
            result += 1
else:
    for i in range(len(R)):
        if R[i] == L[i]:
            if R[i] == '8':
                result += 1
        else:
            break

print(result)
