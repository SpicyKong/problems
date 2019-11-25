# https://www.acmicpc.net/problem/1406 문제 제목 : 에디터 , 언어 : Python, 날짜 : 2019-11-25, 결과 : 성공

import sys
from collections import deque
former = deque(list(sys.stdin.readline()[:-1]))
latter = deque()
N = int(sys.stdin.readline())

for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'P':
        former.append(command[1])
    elif command[0] == 'L':
        try:
            latter.appendleft(former.pop())
        except:
            pass
    elif command[0] == 'D':
        try:
            former.append(latter.popleft())
        except:
            pass
    else:
        try:
            former.pop()
        except:
            pass
print("".join((former + latter)))
