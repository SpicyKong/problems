# https://www.acmicpc.net/problem/7579 문제 제목 : 앱 , 언어 : Python, 날짜 : 2020-06-09, 결과 : 성공
"""
    회고:
    먼저 메모이제이션을 어떻게 할 지 고민하다 비용과 인덱스를 사용하면 될거 같았다. 인덱스를 사용하는 건 최근에 동전 바꿔주기였나? 
    그 문제를 풀면서 알게된 방법이다. 하지만 계속 고민해도 그 다음으로 진전이 없어서 결국 
    다른분의 소스코드를 참고했다. 아래 코드를 간단히 설명하자면 허용 비용을 늘려가면서 M값보다 큰 공간이 확보되는 순간 종료하면 된다.

    어렵다.. 솔직히 이 문제는 풀 수 있을거 같았는데 못푸니깐 아쉽다.
"""

import sys

def dp(now_c, index):
    global N, M, result
    if index >= N:
        return 0
    if not list_memo[index][now_c]==-1:
        return list_memo[index][now_c]
    for n in range(now_c, N*100):
        list_memo[index][n] = dp(n, index+1)
        if list_c[index] <= n:
            list_memo[index][n] = max(list_memo[index][n], list_m[index] + dp(n-list_c[index], index+1))
        if list_memo[index][n] >= M:
            result = n
            break
    return list_memo[index][now_c]


N, M = map(int, sys.stdin.readline().split())
list_m = list(map(int, sys.stdin.readline().split()))
list_c = list(map(int, sys.stdin.readline().split()))
list_memo = [[-1]*(N*100+1) for _ in range(N+1)]
result = 0
dp(0,0)
print(result)
