# https://www.acmicpc.net/problem/2225 문제 제목 : 합분해 , 언어 : Python, 날짜 : 2020-06-07, 결과 : 성공
"""
    회고:
    오랜만에 혼자 풀어본 dp문제 같다. 풀이는 아래와 같다.
    먼저 중복이 발생 되는 부분을 생각해 보았다.
    10을 1가지 수로 표현해보면,
    10 한가지가 있다.
    2가지 수로 표현해보면
    0+10 ~ 10+0까지 있을것이다.
    여기서 두 수중 한개의 수를 쪼개서 생각해보면 이는 3개의 수의 합으로 표현 됨을 알 수 있다.
    ex) 0+10=0+(0+10, 1+9, ... , 10+0)
    
    모든 문제가 이 문제처럼 명확하게 보이진 않겠지만 
    그래도 옛날같았으면 이 문제도 못풀었을테니 뿌듯하다.
"""

import sys

def dp(n, k):
    if list_memo[n][k]:
        return list_memo[n][k]
    if k == 1:
        list_memo[n][k] += 1
        return list_memo[n][k]
    for j in range(n+1):
        list_memo[n][k] += dp(n-j,k-1)
    return list_memo[n][k]
N, K = map(int, sys.stdin.readline().split())
list_memo = [[0]*(K+1) for _ in range(N+1)]
print(dp(N, K)%1000000000)
#[print(a) for a in list_memo]

"""
10
K = 1
10
K = 2
0
1
2
3
4
5
6
7
8
9
10
K=3

"""
