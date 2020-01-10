# https://www.acmicpc.net/problem/2504 문제 제목 : 괄호의 값 , 언어 : Python, 날짜 : 2020-01-10, 결과 : 성공

import sys
list_string = list(sys.stdin.readline().strip())
list_stack = []
list_save = [0]*60
depth = 0
wrong = 0
for value in list_string:
    if value == '(':
        list_stack.append(value)
        depth += 1
    elif value == '[':
        list_stack.append(value)
        depth += 1
    elif value == ')':
        if list_stack and list_stack[-1] == '(':
            depth-=1
            list_stack.pop()
            if list_save[depth + 1]:
                list_save[depth] += list_save[depth + 1] * 2
                list_save[depth + 1] = 0
            else:
                list_save[depth] += 2
        else:
            wrong=1
            break
    elif value == ']':
        if list_stack and list_stack[-1] == '[':
            depth-=1
            list_stack.pop()
            if list_save[depth + 1]:
                list_save[depth] += list_save[depth + 1] * 3
                list_save[depth + 1] = 0
            else:
                list_save[depth] += 3
        else:
            wrong=1
            break
if depth or wrong:
    print(0)
else:
    print(list_save[0])
