# https://www.acmicpc.net/problem/1764 문제 제목 : 듣보잡 , 언어 : Python, 날짜 : 2019-12-09, 결과 : 성공

import sys
N, M = map(int, sys.stdin.readline().split())
list_N = [sys.stdin.readline()[:-1] for _ in range(N)]
list_M = [sys.stdin.readline()[:-1] for _ in range(M)]
list_people = { 'test':0, }
list_result = []
count = 0
for i in range(N):
    list_people[list_N[i]] = 1
for i in range(M):
    try:
        if list_people[list_M[i]]:
            count+=1
            list_result.append(list_M[i])
    except:
        pass
print(count)
[print(name) for name in sorted(list_result)]
