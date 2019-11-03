# https://www.acmicpc.net/problem/1874 문제 제목 : 스택 수열 , 언어 : Python, 날짜 : 2019-11-03, 결과 : 성공
# 역시 안풀릴땐 다음날 찬스

import sys
from collections import deque
N = int(sys.stdin.readline())
list_a = [int(sys.stdin.readline()) for _ in range(N)]
list_b = deque([i+1 for i in range(N)])
list_c = []
list_stack = []
count_stack = 0
count_index = 0
list_print = []
error = 0
while True:
    if count_stack > 0 and list_a[count_index] == list_stack[-1]:
        list_c.append(list_stack.pop())
        list_print.append('-')
        count_index+=1
        count_stack-=1
    elif count_stack > 0 and list_a[count_index] < list_stack[-1]:
        
        error = 1
        break
    elif count_stack > 0 and list_a[count_index] > list_stack[-1]:
        list_stack.append(list_b.popleft())
        list_print.append('+')
        count_stack += 1
    else:
        list_print.append('+')
        list_stack.append(list_b.popleft())
        count_stack += 1
    if count_index == N:
        break
if error == 0:
    [print(a) for a in list_print]
else:
    print('NO')
"""
4 3 6 8 7 5 2 1

1234
123
1256
12578
1257
125
12
1

"""
