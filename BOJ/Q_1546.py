# https://www.acmicpc.net/problem/1546 문제 제목 : 평균 , 언어 : Python, 날짜 : 2019-09-03, 결과 : 성공

import sys
N = int(sys.stdin.readline())
sum_A = 0
list_a = list(map(int, sys.stdin.readline().split()))#[int(sys.stdin.readline()) for _ in range(N)]
max_num = max(list_a)
for a in list_a:
    sum_A+=a/max_num*100
print(sum_A/N)
