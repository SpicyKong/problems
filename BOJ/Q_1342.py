# https://www.acmicpc.net/problem/1342 문제 제목 : 행운의 문자열 , 언어 : Python, 날짜 : 2020-06-04, 결과 : 성공
"""
    회고:
    맨 처음에는 dfs길레 재귀함수로 구현하고 set으로 중복 문자열 체크를 해 주었다.
    그랬더니 메모리 초과가 났다. 그래서 생각해 보았는데, 내가 지금 구현한 코드는 의도치않게 중복 문자열 처리가 되어있었고,
    한번 재귀함수를 반복문으로 바꿔보니깐 pypy3에서 통과했다.

    내가 생각한 핵심(?) 아이디어는 문자열S에서 중복을 제거한 단어들의 리스트를 하나 만들고,
    새로운 리스트를 만들어 기존의 리스트에 있는 단어들의 인덱스와 대응되게 개수를 저장해 그것을 스택에 담아 사용했다.
"""

import sys

s=sys.stdin.readline().strip()
list_caniuse = list(set(list(s)))
dict_count = {a:i for i,a in enumerate(list_caniuse)}
len_s = len(s)
list_first = [0]*len(list_caniuse)

for word in s:
    list_first[dict_count[word]]+=1
result = 0

list_stack = [(' ', 0, list_first)]
while list_stack:
    now_s, now_len, have = list_stack.pop()
    if len_s==now_len:
        result+=1
        continue
    for letter in list_caniuse:
        if not now_s[-1]==letter and have[dict_count[letter]]>0:
            save_have = have[:]
            save_have[dict_count[letter]]-=1
            list_stack.append((now_s+letter, now_len+1, save_have))
    
print(result)
