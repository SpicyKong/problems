# https://www.acmicpc.net/problem/2157 문제 제목 : 여행 , 언어 : Python, 날짜 : 2020-03-06, 결과 : 실패
"""
    회고:
    자꾸 메모리초과가 뜬다. 다시한번 시도해봐야겠다.
"""
import sys
N, M, K = map(int, sys.stdin.readline().split())
list_memo = [[] for _ in range(N+1)]
list_memo[1].append([0,0])

for i in range(K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a < b:
        for memo in list_memo[a]:
            if memo[1]+1 <= M:
                list_memo[b].append([memo[0]+c, memo[1]+1])

print(list_memo)
print(max(list_memo[-1],key= lambda a: a[0])[0])
