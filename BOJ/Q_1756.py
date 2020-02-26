# https://www.acmicpc.net/problem/1756 문제 제목 : 피자 굽기 , 언어 : Python, 날짜 : 2020-02-26, 결과 : 성공
"""
  회고:
  처음 시도했을때 문제점은 list_stack을 만드는 과정에서 stack에 push를 할때 최솟값이 아닌 오븐의 현재 반지름을 넣은것이였다.
  이렇게 되면 나중에 피자의 반지름이 오븐보다 작아서 그 자리에 넣어둔다 쳐도 항상 그것이 정답인 보장을 받을수없다.
  왜냐하면 그 자리보다 위에 있는 오븐의 지름이 더 작게되면 피자는 더 밑으로 들어갈수 없기 때문이다.
"""
import sys
from collections import deque
D, N =map(int, sys.stdin.readline().split())
list_radius = list(map(int, sys.stdin.readline().split()))
list_pizza = deque(map(int, sys.stdin.readline().split()))
now_depth = 0
list_stack = []

pizza_r = list_pizza[0]
now_min = list_radius[0]
for r in list_radius:
    if r >= pizza_r:
        if r < now_min:
            now_min = r
            list_stack.append(r)
        else:
            list_stack.append(now_min)

        now_depth+=1
    else:
        break

if list_stack:
    
    pizza_r = list_pizza.popleft()
    while list_stack:
        oven_r = list_stack.pop()
        if oven_r >= pizza_r:
            if list_pizza:
                pizza_r = list_pizza.popleft()
            else:
                break
        now_depth-=1
    if list_pizza:
        print(0)
    else:
        print(now_depth) 
else:
    print(0)
