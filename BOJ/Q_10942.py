# https://www.acmicpc.net/problem/10942 문제 제목 : 팰린드롬? , 언어 : Python, 날짜 : 2020-04-03, 결과 : 성공
"""
    회고:
    팰린드롬역시 많이 들어본 단어였지만 이름부터 무섭게 생긴 탓에 시도해 보지 못했다.
    알고리즘은 당연한 아이디어인데 역시 신기하다. 하지만 이 DP알고리즘은 시간복잡도가 O(N^2)이므로 이 알고리즘말고도
    Manacher 알고리즘이라는 것도 배워두는 것이 좋겠다.
    이 DP를 이용한 알고리즘의 핵심 아이디어는 양 끝값이 같고 그 사이의 단어가 팰린드롬이라면 그 단어 여깃 팰린드롬이라는 점이다.
"""
import sys

N = int(sys.stdin.readline())
list_num = list(map(int, sys.stdin.readline().split()))



list_memo = [[0]*(N) for _ in range(N)]
for i in range(N):
    list_memo[i][i] = 1
    if N >= 2:
        if (i+1<N and list_num[i] == list_num[i+1]):
            list_memo[i][i+1] = 1
if N > 2:
    for i in range(2,N):
        for j in range(N-i):
            if list_num[j] == list_num[j+i] and list_memo[j+1][j+i-1]:
                list_memo[j][j+i] = 1

M = int(sys.stdin.readline())
for _ in range(M):
    s,e = map(int, sys.stdin.readline().split())
    print(list_memo[s-1][e-1])
#[print(a) for a in list_memo]
"""
1 2 3 4 5 6 7

1 2 1 3 1 2 1

1 2 1
    1 3 1
        1 2 1
  2 1 3 1 2
1 2 1 3 1 2 1

"""
