# https://www.acmicpc.net/problem/9663 문제 제목 : N-Queen , 언어 : Python, 날짜 : 2020-03-26, 결과 : 성공
"""
    회고:
    원래 1799 비숍이라는 문제를 풀려고 하다가 백트레킹 문제의 기본인 N-Queen문제를 안풀어봐서
    한번 풀어보았다. 일단 백트레킹의 흐름은 이해하겠는데 이걸 코드로 구현하려고 하니깐 너무 막막했다.
    그래서 여러 다른분들의 코드를 보면서 어떤식으로 코드를 작성하셨는지 익힌 후에 직접 풀어 보았다.
    대각선 두개와 세로 혹은 가로에 대한 배열 3가지를 선언해 푸는 방식은 정말 신기했다. 어떻게 이런생각들을
    할수있는건지 모르겠다..ㅠㅠ
    아 어제 소마 온라인 코테가 통과했다. 내가 푼 문제수를 생각해보면 전산오류가 아닌지 의심해봐야겠지만 일단 통과한 만큼
    오프라인 코테를 볼수있는 자격은 주어졌다. 코로나 때문에 가기 힘들수도 있겠지만 한번 열심히 준비는 해봐야겠다.
"""

import sys
def DFS(now_x):
    global result
    if now_x == N:
        result += 1
        return
    for now_y in range(N):
        if not(list_x[now_y] or list_slash[now_x+now_y] or list_slash_r[N-1-now_x + now_y]):# == 0:
            list_x[now_y] = 1
            list_slash[now_x+now_y] = 1
            list_slash_r[N-1-now_x + now_y] = 1
            DFS(now_x+1)
            list_x[now_y] = 0
            list_slash[now_x+now_y] = 0
            list_slash_r[N-1-now_x + now_y] = 0
N = int(sys.stdin.readline())
result = 0
list_x = [0]*N
list_slash = [0]*(2*N-1)
list_slash_r = [0]*(2*N-1)
DFS(0)

print(result)
