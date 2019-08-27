# https://www.acmicpc.net/problem/9012 문제 제목 : 괄호 , 언어 : Python, 날짜 : 2019-08-27, 결과 : 성공

import sys
for _ in range(int(sys.stdin.readline())):
    re = True
    list_a = []
    for text in sys.stdin.readline():
        if text == '(':
            list_a.append('(')
        elif len(list_a) > 0 and text == ')':
            list_a.pop()
        elif len(list_a) == 0 and text == ')':
            re = False
            break
    if len(list_a) > 0:
        re = False
    if re == True:
        print('YES')
    else:
        print('NO')
