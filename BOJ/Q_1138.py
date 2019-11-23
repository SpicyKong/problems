# https://www.acmicpc.net/problem/1138 문제 제목 : 한 줄로 서기 , 언어 : Python, 날짜 : 2019-11-23, 결과 : 성공
# 오늘 밖에서 너무 오래있어서 플밍을 못했다. 내일은 더 빡시게 

import sys
N = int(sys.stdin.readline())
list_a = list(map(int, sys.stdin.readline().split()))
list_b = [0]*N

for i,j in enumerate(list_a):
    count = 0
    for k in range(N):
        if list_b[k] == 0:
            if count == j:
                list_b[k] = i+1
            count+=1

[print(a,end=" ") for a in list_b]
