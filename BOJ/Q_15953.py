# https://www.acmicpc.net/problem/15953 문제 제목 : 상금 헌터 , 언어 : Python, 날짜 : 2019-08-22, 결과 : 성공

import sys

N = int(sys.stdin.readline())
reward = {1: 500, 2: 300, 3 :200, 4: 50, 5:30, 6: 10, 7: 0}
for _ in range(N):
    reward_a = 0
    reward_b = 0
    a, b = map(int, sys.stdin.readline().split())
    if 1<= a<=21:
        for n_1 in range(1,7):
            if n_1*(n_1+1)/2 >= a:
                reward_a = int(reward[n_1])
                break
    if 1 <= b <= 31:
        for n_2 in range(1,8):
            if (1-2**(n_2))*(-1) >= b:
                reward_b = 2**(10-n_2)
                break
    print((reward_a + reward_b)*10000)
