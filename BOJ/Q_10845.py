# https://www.acmicpc.net/problem/10845 문제 제목 : 큐 , 언어 : Python, 날짜 : 2019-11-14, 결과 : 성공

import sys
from collections import deque

list_queue = deque()
count = 0

for _ in range(int(sys.stdin.readline())):
    input_a = sys.stdin.readline().split()
    
    if input_a[0] == 'push':
        list_queue.append(int(input_a[1]))
        count += 1
    elif input_a[0] == 'pop':
        if count > 0:
            print(list_queue.popleft())
            count -= 1
        elif count == 0:
            print(-1)
    elif input_a[0] == 'size':
        print(count)
    elif input_a[0] == 'empty':
        if count == 0:
            print(1)
        else:
            print(0)
    elif input_a[0] == 'front':
        if count == 0:
            print(-1)
        else:
            print(list_queue[0])
    elif input_a[0] == 'back':
        if count == 0:
            print(-1)
        else:
            print(list_queue[-1])
