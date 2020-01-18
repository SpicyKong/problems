# https://www.acmicpc.net/problem/2819 문제 제목 : 상근이의 로봇 , 언어 : Python, 날짜 : 2020-01-19, 결과 : 성공
# 내가 짠 소스코드지만 자고일어나면 뭘 의도한건지 하나도 모를거같다..
# 코딩 잘하고싶다.

import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
list_points = []
x_n = []
x_p = []
sum_xn = 0
sum_xp = 0
count_xp = 0
count_xn = 0

y_n = []
y_p = []
sum_yn = 0
sum_yp = 0
count_yn = 0
count_yp = 0
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    if x<0:
        x_n.append(x)
        sum_xn -= x
        count_xn += 1
    elif x >= 0:
        x_p.append(x)
        sum_xp += x
        count_xp += 1
    if y<0:
        y_n.append(y)
        sum_yn -= y
        count_yn += 1
    elif y >= 0:
        y_p.append(y)
        sum_yp += y
        count_yp += 1
x_n = deque(sorted(x_n))
x_p = deque(sorted(x_p))
y_n = deque(sorted(y_n))
y_p = deque(sorted(y_p))
x_p.append(1000002)
y_p.append(1000002)
x_n.appendleft(1000002)
y_n.appendleft(1000002)

now_x = 0
now_y = 0
for direction in list(sys.stdin.readline().strip()):
    if direction == 'S':
        now_y += 1
        if not y_p[0] == 1000002:
            if now_y > y_p[0]:
                save_num = y_p[0]
                while (save_num == y_p[0]):
                    y_n.append(y_p.popleft())
                    count_yp-=1
                    count_yn+=1
        sum_yn += count_yn
        sum_yp -= count_yp
            
    elif direction == 'J':
        now_y -= 1
        if not y_n[-1] == 1000002:
            if now_y < y_n[-1]:
                save_num = y_n[-1]
                while (save_num == y_n[-1]):
                    y_p.appendleft(y_n.pop())
                    count_yp+=1
                    count_yn-=1
        sum_yn -= count_yn
        sum_yp += count_yp
            
    elif direction == 'I':
        now_x += 1
        if not x_p[0] == 1000002:
            if now_x > x_p[0]:
                save_num = x_p[0]
                while (save_num == x_p[0]):
                    x_n.append(x_p.popleft())
                    count_xp-=1
                    count_xn+=1
        sum_xn += count_xn
        sum_xp -= count_xp

    elif direction == 'Z':
        now_x -= 1
        if not x_n[-1] == 1000002:
            if now_x < x_n[-1]:
                save_num = x_n[-1]
                while (save_num == x_n[-1]):
                    x_p.appendleft(x_n.pop())
                    count_xp+=1
                    count_xn-=1
        sum_xn -= count_xn
        sum_xp += count_xp
    print(sum_xn + sum_xp + sum_yp + sum_yn)
