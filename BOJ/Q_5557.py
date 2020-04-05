import sys
"""
    회고:
    아쉽다.. DP를 어떻게 진행할지에 대해서는 생각했는데 막상 구현한 코드가 의도대로 작동하질 않아서 정답코드를 참고했다.
    다른분의 코드를 보고 재귀함수에서 1군데만 손을 봐줬더니 정답이 되었다.

    내가 생각한 방식은 유효한 범위내에서 +와 -를 모두 테스트 해보다가 총합이 마지막 값과 같아지면 업데이트를 해주는 방식이다.
    사실 이 생각때문에 재귀함수로 짜려도 한건데 반복문으로 짜는코드도 있어서 신기했다. 해결할수있었는데 아쉬움이 크다.
    나도 이제 1일 1DP를 시작해야겠다.
    
    주석은 고치기 전 코드다.
    """
def go(now_result, n):
    global result, N, list_num, list_dp
    #print(n, now_result, list_num[n+1])
    if now_result < 0 or now_result > 20:
        return 0
    if n == N-2:
        return list_num[-1] == now_result
    
    if list_dp[n][now_result]:
        return list_dp[n][now_result]


    list_dp[n][now_result] += go(now_result+list_num[n+1], n+1)
    list_dp[n][now_result] += go(now_result-list_num[n+1], n+1)
    return list_dp[n][now_result]
    #if go(now_result+list_num[n+1], n+1):
    #    print('+')
    #    list_dp[n][now_result] += list_dp[n+1][now_result+list_num[n+1]]
    #
    #if go(now_result-list_num[n+1], n+1):
    #    print('-')
    #    list_dp[n][now_result] += list_dp[n+1][now_result-list_num[n+1]]

    

N = int(sys.stdin.readline())
list_num = list(map(int, sys.stdin.readline().split()))
list_dp = [[0]*(21) for _ in range(N)]
result = 0
go(list_num[0], 0)
#print(list_dp[0])
#print(list_dp[0])
#[print(a) for a in list_dp]
print(list_dp[0][list_num[0]])
"""
11
8 3 2 4 8 7 2 4 0 8 7

11
8 3 2 4 8 7 2 4 0 8 8
"""
