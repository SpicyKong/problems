# https://www.acmicpc.net/problem/1613 문제 제목 : 역사 , 언어 : Python, 날짜 : 2020-05-03, 결과 : 성공
"""
    회고:
    플로이드 워셜로 풀고 python3 로 제출하니깐 시간 초과가 뜬다.. 그래서 결국 pypy3로 제출했다.
    이 문제는 플로이드 워셜로 값을 계속 갱신해 나가면 되는 문제다. 
    기존의 플로이드 워셜보다는 아주 조금 더 생각을 해줘야 하기는 하지만 난이도가 높지는 않다.

    오늘 레몬과 라임을 포트에서 화분으로 이사시켜주었다. 근데 레몬이 지금보니 잔뿌리가 다 뽑혀있던데 아마도 판매하시는 분께서 포트에서 키운게 아니라
    땅에서 키우시던걸 포트로 옮긴거 같다.. 일단 물을 주고 지켜봐야겠다. 레몬은 한동안 분갈이 몸살이 올거같다.
    
"""

import sys
n, k = map(int, sys.stdin.readline().split())
list_map = [[0]*n for _ in range(n)]
for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    list_map[a-1][b-1] = -1
    list_map[b-1][a-1] = 1

for mid in range(n):
    for start in range(n):
        for end in range(n):
            if mid == start or mid == end or start == end:
                continue
            if list_map[start][end] == 0 and (list_map[start][mid] * list_map[mid][end]):
                if list_map[start][mid] + list_map[mid][end] > 0:
                    list_map[start][end] = 1
                elif list_map[start][mid] + list_map[mid][end] < 0:
                    list_map[start][end] = -1


r = int(sys.stdin.readline())
for _ in range(r):
    a, b = map(int, sys.stdin.readline().split())
    print(list_map[a-1][b-1])
