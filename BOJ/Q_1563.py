# https://www.acmicpc.net/problem/1563 문제 제목 : 개근상 , 언어 : Python, 날짜 : 2020-06-30, 결과 : 성공
"""
    회고:
    맨 처음에 dp를 어떻게 할까 고민하다가, [몇일][출석정보][지각횟수]라고 생각하고 짜기 시작했는데
    문제를 다시 읽어보니 결석이 3번 연속이상이면 개근상의 조건에 부합하지 않았던것이였다.
    그래서 연속인것을 어떻게 처리할지 고민하다가 결국 다른분의 코드를 참고해서 풀었다.
    다른분의 코드를 보니 내가 기존에 생각했던 출석정보 대신 연속 결석 일수를 이용하는것이 핵심이었다.
    대충 느낌은 알아가는것 같다.
"""

import sys
sys.setrecursionlimit(10000)
N = int(sys.stdin.readline())
"""
No 개근:
    1. 지각 두번이상
    2. 결석 세 번 연속
O 출석
A 결석
L 지각
list[몇일][연속결석일수][지각횟수]
"""
def dp(n,cn, ln):
    if cn>2 or ln>1:
        return 0
    elif n==N:
        return 1
    elif not list_memo[n][cn][ln] == -1:
        return list_memo[n][cn][ln]
    list_memo[n][cn][ln]= 0
    list_memo[n][cn][ln]+=dp(n+1, 0, ln)
    list_memo[n][cn][ln]+=dp(n+1, cn+1, ln)
    list_memo[n][cn][ln]+=dp(n+1, 0, ln+1)
    list_memo[n][cn][ln]%=1000000
    return list_memo[n][cn][ln]
    

list_memo = [[[-1,-1] for _ in (0,0,0)] for _ in range(N+1)]

print(dp(0,0,0))
