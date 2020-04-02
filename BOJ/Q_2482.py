# https://www.acmicpc.net/problem/2482 문제 제목 : 색상환 , 언어 : Python, 날짜 : 2020-04-02, 결과 : 성공
"""
    회고:
    오랜만에 온전히 내 머릿속에서 나온 풀이였다. 심지어 그 문제가 DP라니.. 기분이 매우 좋다ㅋㅋ
    우선 점화식을 찾기 위해 N=1 부터 7부터 적고 멍때리다가 점화식을 발견했다. 바로 아래의 식이였다.
    dp[N][K] = dp[N-1][K] + dp[N-2][K-1] 
    그리고 이 식대로 바텀업 방식으로 풀이를 작성하고 제출했더니 정답이였다. 사실 맨처음에 메모이제이션을 하는 배열의 크기를 잘못잡아서
    런타임에러가 나기는 했다. 어쨋거나 기분이 좋다. 나중에 한번 탑다운 방식으로도 풀어봐야겠다.
"""
import sys

# dp[N][K] = dp[N-1][K] + dp[N-2][K-1]

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
list_memo = [[0]*(N+1) for _ in range(N+1)]
list_memo[2][1] = 2
list_memo[3][1] = 3

for n in range(4,N+1):
    for k in range(1,n//2+1):
        if k == 1:
            list_memo[n][k] = n
        else:
            list_memo[n][k] = list_memo[n-1][k] + list_memo[n-2][k-1]
print(list_memo[N][K]%1000000003)
