# https://www.acmicpc.net/problem/5397 문제 제목 : 키로거 , 언어 : Python, 날짜 : 2019-09-29, 결과 : 성공

from collections import deque
M = int(input())
for _ in range(M):
    list_former = deque()
    list_later = deque()
    list_key = list(input())
    
    for key in list_key:
        if key == '<':
            if list_former:
                list_later.appendleft(list_former.pop())
        elif key == '>':
            if list_later:
                list_former.append(list_later.popleft())
        elif key == '-':
            if list_former:
                list_former.pop()
        else:
            list_former.append(key)
    print("".join(list_former+list_later))
