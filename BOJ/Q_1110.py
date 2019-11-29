# https://www.acmicpc.net/problem/1110 문제 제목 : 더하기 사이클 , 언어 : Python, 날짜 : 2019-11-29, 결과 : 성공

import sys
N = int(sys.stdin.readline())
goal = N
if N < 10:
    N= '0' + str(N)
else:
    N = str(N)
sum_save = 0
for n in N:
    sum_save+=int(n)
N = int(N[-1] + str(sum_save)[-1])
count = 1
while not goal == N:
    count+=1
    if N < 10:
        N= '0' + str(N)
    else:
        N = str(N)
    sum_save = 0
    for n in N:
        sum_save+=int(n)
    N = int(N[-1] + str(sum_save)[-1])
print(count)
