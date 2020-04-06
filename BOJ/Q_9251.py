# https://www.acmicpc.net/problem/9251 문제 제목 : LCS , 언어 : Python, 날짜 : 2020-04-06, 결과 : 성공
"""
    회고:
    벌써 몇번째 디피문제 구현에서 무너지는지 모르겠다.. 나는 최근 푸는 디피 문제들을 풀때 아이패드에 대충 흐름을 적어놓고 푸는데
    실제 정답 코드와 내가 생각한 방식이 유사한데도 자꾸 구현에서 막힌다. 아마도 아이패드에 풀이법을 구상하는 단계에서 너무 추상화해서 이런 실수를 하는건지도 모르겠다.
    이제 진짜로 좀더 자세하게 적어서 내일 푸는 문제는 안보고 풀거다.
    내가 생각한 풀이 방법은 N*M 크기의 메모이제이션용 배열을 만들고 같은것이 있으면 +1 해주는게 기본이다. 그리고 대각선 위에 있는 값을 더해준다(지금까지의 최대값이다 이게)
    하지만 같은게 없어도 다음 배열에서는 기존에 구했던 최대값이 필요하므로 업데이트를 안했더라면 왼쪽값과 위에값중 더 큰값을 집어넣으면 된다.
    아쉽다. 나도 알리고즘 잘하고싶다.
"""

import sys

string1 = sys.stdin.readline().strip()
string2 = sys.stdin.readline().strip()

if len(string1) < len(string2):
    swap = string1
    string1 = string2
    string2 = swap
N = len(string1)
M = len(string2)

list_dp = [[0]*(M) for _ in range(N)]
for n1 in range(N):
    for n2 in range(M):

        if string1[n1] == string2[n2]:
            list_dp[n1][n2] += 1
            if n1 and n2:
                list_dp[n1][n2] += list_dp[n1-1][n2-1]
        else:
            if n1:
                list_dp[n1][n2] = max(list_dp[n1][n2], list_dp[n1-1][n2])
            if n2:
                list_dp[n1][n2] = max(list_dp[n1][n2-1], list_dp[n1][n2])
print(list_dp[N-1][M-1])
