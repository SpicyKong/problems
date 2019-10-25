# https://www.acmicpc.net/problem/2581 문제 제목 : 소수 , 언어 : Python, 날짜 : 2019-10-25, 결과 : 성공

import sys
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
list_num = [i for i in range(10001)]
list_check = [0 for i in range(10001)]
list_num[1] = 0
for n in range(2,101):
    count = 2
    while count*n <= 10000:
        if list_check[n*count] == 0:
            list_check[n*count] =1
            list_num[n*count] = 0
        count+=1
a = sum(list_num[M:N+1])
if a==0:
    print(-1)
else:
    print(a)
    for i in range(M,N+1):
        if list_num[i] > 0:
            print(list_num[i])
            break
