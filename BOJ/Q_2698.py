# https://www.acmicpc.net/problem/2698 문제 제목 : 인접한 비트의 개수 , 언어 : Python, 날짜 : 2020-04-08, 결과 : 성공
"""
    회고:
    점화식을 세우는데 오래걸렸다. 맨처음에는 그냥 끝자리에 상관없이 생각했는데 생각해보니 이러면 각각의 저장된 연결된 비트쌍이 늘어나는지
    그대로인지 알 도리가 없다. 그래서 0,1로 끝나는 경우를 각각 나눠주고 실행시키니 맞게되었다. 오랜만에 혼자 푼거같다ㅋㅋ
    
    근데 오늘 새벽 강의를 4시까지 듣느냐고 너무 피곤해서 점화식 세우다가 몇번이나 졸았다.
    학교 강의 서버가 좋지 못해 낮에는 버퍼링 때문에 못듣는다..ㅠㅠ
    오늘과 어제는 손목부상으로 쉬는날이였다고 생각하고 내일부턴 다시 열심히 해야겠다.

"""

import sys
T = int(sys.stdin.readline())
list_memo = [[[0]*2 for _ in range(101)] for _ in range(101)]
list_memo[1][1] = [1,1]
for n in range(1,101):
    for k in range(1,n+1):
        if n == 1 and k == 1:
            continue
        list_memo[n][k][0] = list_memo[n-1][k][0] + list_memo[n-1][k][1]
        list_memo[n][k][1] = list_memo[n-1][k][0] + list_memo[n-1][k-1][1]
#[print(a) for a in list_memo]
for _ in range(T):
    n, k = map(int, sys.stdin.readline().split())
    print(sum(list_memo[n][k+1]))
