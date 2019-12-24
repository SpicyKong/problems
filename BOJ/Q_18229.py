# https://www.acmicpc.net/problem/18229 문제 제목 : 내가 살게, 아냐 내가 살게 , 언어 : Python, 날짜 : 2019-12-24, 결과 : 성공

import sys
def func_18229():
    N, M, K = map(int, sys.stdin.readline().split())
    list_hand = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    list_hand_sum = [0]*(N)
    for i in range(M):
        for j in range(N):
            list_hand_sum[j]+=list_hand[j][i]
            if list_hand_sum[j] >= K:
                print(j+1,i+1)
                return
func_18229()
