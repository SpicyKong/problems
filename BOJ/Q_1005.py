# https://www.acmicpc.net/problem/1005 문제 제목 : ACM Craft , 언어 : Python, 날짜 : 2020-04-03, 결과 : 성공
"""
    회고:
    위상정렬이 순서를 표현할때 쓴다는 사실은 알고 있었지만 그동안 배울생각은 없이 지나쳐 왔다. 그러던중 무엇을 풀까 고민하다
    백준 문제풀기를 시작한지 일주일도 안되었을때 시도해봤던 이 문제를 보았다. (그때 그림까지 그려가면서 풀어보려고 애썼지만 정작 풀지는 못했다ㅋㅋ)
    가장 핵심은 진입차수에 대한 아이디어인것 같다. 위상정렬이라는 검색어로 검색을 한 후 나왔던 자료에서 진입차수에 대한 아이디어만 얻고 이 문제를 풀었는데
    한번에 쫘라락 맞으니 신기하다. 역시 세상에는 똑똑한 사람들이 너무 많은것 같다.

    P.S. 예전에 내가 이 문제를 풀수있는 날이 올까? 라는 생각을 가지곤 했는데
         그 날이 오늘일때는 정말 뿌듯함을 느끼는것 같다.
"""

import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    list_delay = list(map(int, sys.stdin.readline().split()))
    list_check = [[0,list_delay[i-1]] for i in range(N+1)]
    list_map = [[] for _ in range(N+1)]
    for _ in range(K):
        a, b = map(int, sys.stdin.readline().split())
        list_map[a].append(b)
        list_check[b][0] += 1
    W = int(sys.stdin.readline())
    list_queue = deque()
    for i, num in enumerate(list_check):
        if not i:
            continue
        if not num[0]:
            list_queue.append([list_delay[i-1], i])
    while list_queue:
        now_cost, now_index = list_queue.popleft()
        if now_index == W:
            break
        for next_index in list_map[now_index]:
            list_check[next_index][0] -= 1
            list_check[next_index][1] = max(list_check[next_index][1], now_cost + list_delay[next_index - 1])
            if not list_check[next_index][0]:
                list_queue.append([list_check[next_index][1], next_index])
    print(list_check[W][1])
