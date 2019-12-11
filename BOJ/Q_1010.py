# https://www.acmicpc.net/problem/1010 문제 제목 : 다리 놓기 , 언어 : Python, 날짜 : 2019-12-11, 결과 : 성공
# 이문제는 처음으로 아이패드로 푼 문제다!ㅋㅋ
# 어제풀었던 2xn 타일링2 라는 문제에서 많이 배운것 같다!

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    #pass
    N, M = map(int, sys.stdin.readline().split())
    list_dp = [[0]*(M+1) for _ in range(N+1)]
    for n in range(N+1):
        for m in range(M+1):
            if n==1:
                list_dp[n][m] = m
            elif m==n:
                list_dp[n][m] = 1
            elif not n or not m:
                pass
            else:
                list_dp[n][m] = list_dp[n-1][m-1] + list_dp[n][m-1]
    print(list_dp[N][M])
