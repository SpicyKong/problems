# https://www.acmicpc.net/problem/9466 문제 제목 : 텀 프로젝트 , 언어 : Python, 날짜 : 2020-07-02, 결과 : 성공
"""
    회고:
    dfs태그에 있어서 풀었는데 솔직히 어떤 유형의 문제인지 잘 모르겠다. 
    우선 이문제의 핵심은 사이클을 찾는것이다. 나는 그냥 dfs를 진행하며 지나온 자리(?)를 마킹해주고 만약 내가 방금 지나온 자리를 만났다면 사이클이라고 판정했다.
    그 후 사이클이 형성되었으면 사이클내의 원소의 개수를 리턴해 n값을 그만큼 빼주었다.

    최근들어 내 습관중에 굉장히 좋지 못한 습관이 있다는 것을 알게되었다. 몰라서 못하는게 아니라 안내켜서 못하고 있었다.
    중간, 기말시험때도 그랬고 최근 문제를 풀면서도 그런식으로 시간을 굉장히 많이 허비한다. 이제부터 어떤 문제든 5~10분정도 고민하고
    그냥 더럽게라도 풀어봐야겠다.
"""
import sys
sys.setrecursionlimit(10**6)
def dfs(num, k, c):
    if list_visit[num] == 0:
        list_visit[num] = k
        list_count[num] = c
        return dfs(list_num[num]-1, k, c+1)
    else:
        if list_visit[num] == k:
            return c - list_count[num]
        else:
            return 0

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    list_num = list(map(int, sys.stdin.readline().split()))
    list_visit = [0]*n
    list_count = [0]*n
    for i in range(1, n+1):
        n-=dfs(i-1, i, 1)
    print(n)
"""
1
2
2 1
"""
