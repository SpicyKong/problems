# https://www.acmicpc.net/problem/11727 문제 제목 : 2×n 타일링 2 , 언어 : Python, 날짜 : 2019-12-10, 결과 : 성공
# 이 문제는 처음에 세웠던 점화식이 맞았었는데, 다시생각해보니 아닌거 같아서
# 힘들게 돌아간 문제다..

import sys
N = int(sys.stdin.readline())
list_dp = [0] * (N+1)
if N == 1:
    print(1)
elif N==2:
    print(3)
else:
    list_dp[1] = 1
    list_dp[2] = 3
    for i in range(3,N+1):
        list_dp[i] = (list_dp[i-1]%10007 + (list_dp[i-2]*2)%10007)%10007
print(list_dp[N])
