# https://www.acmicpc.net/problem/1157 문제 제목 : 단어 공부 , 언어 : Python, 날짜 : 2019-08-13, 결과 : 성공

import sys

word = sys.stdin.readline()
list_word = [a.upper() for a in word][:-1]
list_word1 = list(set(list_word))
list_a = [0 for _ in range(len(list_word1))]
for b in list_word:
    list_a[list_word1.index(b)]+=1
max_num = max(list_a)
list_b = [d for d,c in enumerate(list_a) if c == max_num]
if len(list_b) == 1:
    print(list_word1[list_b[0]])
else:
    print('?')
