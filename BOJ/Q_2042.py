# https://www.acmicpc.net/problem/2042 문제 제목 : 구간 합 구하기 , 언어 : Python, 날짜 : 2019-08-21, 결과 : 실패(트리 공부하기)

import sys

N, M, K = map(int,sys.stdin.readline().split())
list_a = []
for _ in range(N):
    list_a.append(int(sys.stdin.readline()))

count_M=0
count_K=0
while True:
    a, b, c = map(int,sys.stdin.readline().split())
    if a==1:
        list_a[b-1]=c
        count_M+=1
    else:
        print(sum(list_a[b-1:c]))
        count_K+=1
    if count_M == M and count_K == K:
        break
