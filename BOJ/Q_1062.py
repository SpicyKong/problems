# https://www.acmicpc.net/problem/1062 문제 제목 : 가르침 , 언어 : Python, 날짜 : 2020-05-22, 결과 : 성공
"""
    회고:
    사실 비트 마스킹을 이용할 생각은 못했었는데 게시판에서 힌트를 얻었다.
    그리고 생각을 해보니 비트마스킹을 사용하면 만들 수 있는 문자인지 확인이 매우 편해져서 나도 비트마스킹을 사용해 보았다.
    그냥 백트레킹으로 완전탐색을 해서 풀었다. 한가지 아쉬운 점은 맨 처음 풀 때 지문을 이해하지 못해서 시간소모를 했다.
"""

import sys

def dfs(now_depth, know_set, start):
    global set_visit, result
    if now_depth <= 0:
        nowc = 0
        for word in list_word:
            #print(word&know_set == word, word&know_set, word)
            if word&know_set == word:
                nowc+=1
        result = max(result, nowc)
        return
    for i in range(start, 26):
        if not know_set>>i&1:
            dfs(now_depth-1, know_set|1<<i, i+1)
N, K = map(int, sys.stdin.readline().split())
if K < 5:
    print(0)
else:
    K-=5
    list_word = [sys.stdin.readline().strip() for _ in range(N)]
    dict_alpha = {chr(97+i):i for i in range(26)}
    result = 0
    for i, word in enumerate(list_word):
        now = 1 << 26
        for letter in word:
            now |= 1<<dict_alpha[letter]
        list_word[i] = now
    dfs(K, 67641605, 0)
    print(result)
