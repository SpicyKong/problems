# https://www.acmicpc.net/problem/11060 문제 제목 : 점프 점프 , 언어 : Python, 날짜 : 2019-12-21, 결과 : 성공
# dp문제중 가장 짧은시간이 걸린문제ㄷㄷ
# 아래와 같은 반례를 조심하자 (게시판을 보고 나서야 알았다..)
# 5
# 1 0 0 1 0
# 위 반례 해결법 : dp[1]의 값을 1로 초기화 한후 최종결과에서 1만큼 빼준다. 
# 그 이유는 dp[i]의 값이 0일경우 i번째 미로에는 도착할수 없는것이므로 무시해주어야 한다.
# 하지만 그냥 dp[i] == 0이런식으로 검증할 경우 시작조차 못하기때문에 초기값을 0으로 설정한후
# 결과값에서 1을 빼주는 방법을 생각했다.

import sys
N = int(sys.stdin.readline())
list_maze = [0] + list(map(int, sys.stdin.readline().split()))
list_dp = [0] * (N+1)
list_dp[1] = 1
#list_dp[1] = 0
for i in range(1,N+1):
    if list_dp[i]:
        for j in range(1,list_maze[i]+1):
            if i + j <= N:
                if not list_dp[i+j]:
                    list_dp[i+j] += list_dp[i] + 1
                else:
                    if list_dp[i+j] > list_dp[i] + 1:
                        list_dp[i+j] = list_dp[i] + 1
if list_dp[-1]:
    print(list_dp[-1] - 1)
else:
    print(-1)
