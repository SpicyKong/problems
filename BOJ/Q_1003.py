# https://www.acmicpc.net/problem/1003 문제 제목 : 피보나치 함수 , 언어 : Python, 날짜 : 2019-10-12, 결과 : 성공

import sys
N = int(sys.stdin.readline())
num_zero = 0
num_one = 0
list_dp = [0,1,1]
last_num = 2
for i in range(N):
    num_zero, num_one =0,0
    num = int(sys.stdin.readline())
    if num > last_num:
        for a in range(num - last_num):
            list_dp.append(list_dp[-1] + list_dp[-2])
    if num == 0:
        print(1, 0)
    else:
        print(list_dp[num-1], list_dp[num])
