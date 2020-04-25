# https://www.acmicpc.net/problem/2240 문제 제목 : 자두나무 , 언어 : Python, 날짜 : 2020-04-25, 결과 : 성공 
"""
    회고:
    DP문제를 풀어보았다. DP는 티어가 조금만 높아도 너무 어렵게 느껴져서 약간 낮은 티어의 문제를 선정했다. 
    이 문제에서 살펴봐야할 키워드를 선정하자면 [시간, 이동횟수, 위치]이다. 그리고 이 3가지에 대해서 생각을 해보며
    점화식을 세우고 메모이제이션을 하면 된다. 문제의 난이도에 비해 시간이 오래걸렸다. 저 키워드를 생각해내는데 오래걸린것 같다.
    
    내일 소마 2차 온라인 코테가 있기는 한데 알고리즘도 그렇고, 특히 웹스택 관련 해서는 지식이 전무해 이번 2020년에 좀더 공부를 한 다음 내년에는 제대로 도전해봐야 겠다.
"""

import sys

T, W= map(int, sys.stdin.readline().split())
list_jadu = [int(sys.stdin.readline()) for _ in range(T)]
list_memo = [[[0,0] for _ in range(W+2)] for _ in range(T)]
if list_jadu[0] == 1:
    list_memo[0][W][0] = 1
else:
    list_memo[0][W-1][1] = 1
now_max = 1
for t in range(1, T):
    for w in range(W+1):
        list_memo[t][w][0] = max(list_memo[t-1][w][0], list_memo[t-1][w+1][1])
        list_memo[t][w][1] = max(list_memo[t-1][w][1], list_memo[t-1][w+1][0])
        if list_jadu[t]-1:
            list_memo[t][w][1] += 1
        else:
            list_memo[t][w][0] += 1
        now_max = max(now_max, list_memo[t][w][0], list_memo[t][w][1])

            
print(now_max)
